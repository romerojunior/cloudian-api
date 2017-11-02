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


class BaseComponent(object):

    """Defines the base class for each component."""

    base_url = None

    def __init__(self, requestor):
        """ Constructor only contains an instance of HttpRequestor.

        :param requestor:   instance of an HTTP request manager
        :type requestor:    HttpRequestor
        :rtype:             BaseComponent
        """
        self.requestor = requestor

    def __getattr__(self, endpoint):
        # closure, expects keyword argument unpacking:
        def handler(**parameters):
            return self._inner_getattr(endpoint, **parameters)
        return handler

    def _inner_getattr(self, endpoint, **parameters):
        """ Fetches the API endpoints and all URL parameters in order to
        construct a valid Cloudian Admin API call.

        :param endpoint:    the endpoint path (without parameters)
        :type endpoint:     str
        :param parameters:  URL query parameters
        :type parameters:   dict
        :rtype:             BaseComponent
        """
        api_call = '/{base_url}/{endpoint}'.format(
            base_url=self.__class__.base_url,
            endpoint=endpoint
        )

        for index, (key, value) in enumerate(parameters.items()):
            # builds a valid API call with proper URL syntax:
            symbol = '&' if index else '?'

            api_call += '{symbol}{key}={value}'.format(
                symbol=symbol, key=key, value=value
            )

        return self.requestor.http_get(api_call)
