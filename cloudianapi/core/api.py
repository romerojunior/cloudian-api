#!/usr/bin/env python
# -*- coding:utf8 -*-

#      Copyright 2017, Schuberg Philis BV
#
#      Licensed to the Apache Software Foundation (ASF) under one
#      or more contributor license agreements.  See the NOTICE file
#      distributed with this work for additional information
#      regarding copyright ownership.  The ASF licenses this file
#      to you under the Apache License, Version 2.0 (the
#      "License"); you may not use this file except in compliance
#      with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing,
#      software distributed under the License is distributed on an
#      "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#      KIND, either express or implied.  See the License for the
#      specific language governing permissions and limitations
#      under the License.

#      Romero Galiza Jr. - rgaliza@schubergphilis.com


import requests
import urllib3


class CloudianREST(object):

    """Defines a basic REST API client to be extended by components."""

    def __init__(self, admin_url, port, api_user, api_key):
        """ CloudianREST constructor, requires information regarding the admin
        API server provided by Cloudian Inc. Hyperstore.

        :param admin_url:   the admin url configured on your hyperstore cluster
        :type admin_url:    str
        :param port:        TCP port configured to listen HTTP/S requests
        :type port:         int
        :param api_user:    admin API user configured on your cluster
        :type api_user:     str
        :param api_key:     API key configured on your cluster
        :type api_key:      str
        :rtype:             CloudianREST
        """
        self.admin_url = admin_url
        self.port = port
        self.api_user = api_user
        self.api_key = api_key

    def http_get(self, call_str):
        """ Builds a request and fetches its response from the admin API
        server, returns a JSON encoded string.

        :param call_str:    the endpoint with all parameters to GET request
        :type call_str:     str
        :rtype:             str
        """
        urllib3.disable_warnings()

        try:
            api_call = '{admin_url}:{port}/{call}'.format(
                admin_url=self.admin_url,
                port=self.port,
                call=call_str
            )

            response = requests.get(api_call, verify=False,
                                    auth=(self.api_user, self.api_key)
                                    )

            if response.status_code == 200:
                return response.json()

            else:
                print("Error: Request response code %s (%s)" %
                      (response.status_code, response.reason))
                exit(1)

        except ValueError as err:
            print("Error: " + str(err.message))
            exit(1)

        except urllib3.exceptions.ConnectionError as err:
            print("Error: " + str(err.message))
            exit(1)


class BaseComponent(object):

    base_url = None

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def __getattr__(self, endpoint):

        def handler(**kwargs):
            return self._inner_getattr(endpoint, **kwargs)
        return handler

    def _inner_getattr(self, endpoint, **kwargs):

        api_call = '/{base_url}/{endpoint}'.format(
            base_url=self.__class__.base_url,
            endpoint=endpoint
        )

        if 'nodeId' in kwargs.keys():
            api_call += '?nodeId={node_id}'.format(
                node_id=kwargs['nodeId']
            )

        if 'region' in kwargs.keys():
            api_call += '?region={region}'.format(
                region=kwargs['region']
            )

        return self.rest_client.http_get(api_call)
