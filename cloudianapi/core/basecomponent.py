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

    def __call__(self, **parameters):
        """ Gets a properly built request and queries the Requestor.

        :param parameters:  URL query parameters
        :type parameters:   dict
        :rtype:             BaseComponent
        """
        request = self._build_request(**parameters)

        return self.requestor.request(**request)

    def __getattr__(self, endpoint):
        # closure, expects keyword argument unpacking:
        def handler(**parameters):
            return self._inner_getattr(endpoint, **parameters)
        return handler

    def _inner_getattr(self, endpoint, **parameters):
        """ Gets a properly built request and queries the Requestor.

        :param endpoint:    the endpoint path (without parameters)
        :type endpoint:     str
        :param parameters:  URL query parameters
        :type parameters:   dict
        :rtype:             BaseComponent
        """
        request = self._build_request(endpoint, **parameters)

        return self.requestor.request(**request)

    def _build_request(self, endpoint='', **parameters):
        """ Builds a proper API request.

        :param endpoint:    the endpoint path (without parameters)
        :type endpoint:     str
        :param parameters:  URL query parameters
        :type parameters:   dict
        :rtype:             dict
        """

        request = {
            'method': parameters.pop('method', 'GET'),
            'data': parameters.pop('data', None),
            'json': parameters.pop('json', None)
        }

        base_url = self.__class__.base_url

        if endpoint:
            url = '{base_url}/{endpoint}'.format(
                base_url=base_url,
                endpoint=endpoint
            )
        else:
            url = '{base_url}'.format(
                base_url=base_url,
            )

        for index, (key, value) in enumerate(parameters.items()):
            url += '{symbol}{key}={value}'.format(
                symbol='&' if index else '?', key=key, value=value
            )

        request['url'] = url

        return request
