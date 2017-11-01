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

from cloudianapi.components.billing import *
from cloudianapi.components.bppolicy import *
from cloudianapi.components.group import *
from cloudianapi.components.monitor import *
from cloudianapi.components.qos import*
from cloudianapi.components.ratingplan import *
from cloudianapi.components.system import *
from cloudianapi.components.tiering import *
from cloudianapi.components.usage import *
from cloudianapi.components.user import *
from cloudianapi.components.whitelist import *

from cloudianapi.core.api import CloudianREST


class CloudianAPIClient(object):

    def __init__(self, url, port, user, key):

        # CloudianAPIClient has private attributes:
        self._url = url
        self._port = port
        self._api_user = user
        self._key = key

        # CloudianAPIClient has a private REST manager:
        self._rest_client = CloudianREST(self._url,
                                         self._port,
                                         self._api_user,
                                         self._key)

        # CloudianAPIClient has components:
        self.billing = Billing(self._rest_client)
        self.bppolicy = BucketPolicy(self._rest_client)
        self.group = Group(self._rest_client)
        self.monitor = Monitor(self._rest_client)
        self.qos = Qos(self._rest_client)
        self.ratingPlan = RatingPlan(self._rest_client)
        self.system = System(self._rest_client)
        self.tiering = Tiering(self._rest_client)
        self.usage = Usage(self._rest_client)
        self.user = User(self._rest_client)
        self.whitelist = Whitelist(self._rest_client)

