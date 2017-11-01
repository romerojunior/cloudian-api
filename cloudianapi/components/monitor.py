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

from cloudianapi.core.api import CloudianREST


class Monitor(CloudianREST):

    base_url = 'monitor'

    def __getattr__(self, endpoint):

        def handler(**kwargs):
            return self._inner_getattr(endpoint, **kwargs)
        return handler

    def _inner_getattr(self, endpoint, **kwargs):

        api_call = '/{base_url}/{endpoint}'.format(
            base_url=Monitor.base_url,
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

        return self.http_get(api_call)


if __name__ == '__main__':

    api_url = "http://admin.storage.acc.schubergphilis.com"
    api_port = 18081
    api_user = "apiuser"
    api_key = "OI7ELeGsw2"

