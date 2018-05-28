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


class HttpRequestor(object):

    """Defines a basic REST API client to be extended by components."""

    def __init__(self, url, port, user, key, warn=False):
        """ CloudianREST constructor, requires information regarding the admin
        API server provided by Cloudian Inc. Hyperstore.

        :param url:         the admin url configured on your hyperstore cluster
        :type url:          str
        :param port:        TCP port configured to listen HTTP/S requests
        :type port:         int
        :param user:        admin API user configured on your cluster
        :type user:         str
        :param key:         API key configured on your cluster
        :type key:          str
        :param warn:        if set to True, warnings are enabled
        :type warn:         bool
        :rtype:             HttpRequestor
        """
        self.url = url
        self.port = port
        self.user = user
        self.key = key
        self.warn = warn

    def request(self, url, data=None, json=None, method='GET'):
        """ Builds a request and fetches its response from the admin API
        server, returns a JSON encoded string. SSL verification is disabled.
        Simply put: this method works as a request.requests() wrapper.

        :param url:    the endpoint with all parameters to GET request
        :type url:     str
        :param method:      HTTP method (GET, POST, HEAD, DELETE, etc)
        :type method:       str
        :param data:        file-like object to send in the body of the request
        :type data:         dict
        :param json:        json data to send in the body of the request
        :type json:         dict
        :rtype:             str
        """
        if not self.warn:
            requests.urllib3.disable_warnings()

        api_call = '{url}:{port}/{call}'.format(
            url=self.url, port=self.port, call=url
        )

        response = requests.request(
            verify=False,
            method=method,
            url=api_call,
            data=data,
            json=json,
            auth=(
                self.user, self.key
            ),
        )
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                # GET /system/version
                return response.text
        else:
            return {
                'reason': response.reason,
                'status_code': response.status_code,
                'url': response.request.url
            }
