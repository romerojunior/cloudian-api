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

from cloudianapi.components.billing import Billing
from cloudianapi.components.bppolicy import BucketPolicy
from cloudianapi.components.group import Group
from cloudianapi.components.monitor import Monitor
from cloudianapi.components.qos import Qos
from cloudianapi.components.ratingplan import RatingPlan
from cloudianapi.components.system import System
from cloudianapi.components.tiering import Tiering
from cloudianapi.components.usage import Usage
from cloudianapi.components.user import User
from cloudianapi.components.whitelist import Whitelist

from cloudianapi.core.requestors import HttpRequestor


class CloudianAPIClient(object):

    def __init__(self, url, port, user, key):

        # CloudianAPIClient has private attributes:
        self._url = url
        self._port = port
        self._api_user = user
        self._key = key

        # CloudianAPIClient has a private REST manager:
        self._requestor = HttpRequestor(self._url,
                                        self._port,
                                        self._api_user,
                                        self._key)

        # CloudianAPIClient has components:
        self.billing = Billing(self._requestor)
        self.bppolicy = BucketPolicy(self._requestor)
        self.group = Group(self._requestor)
        self.monitor = Monitor(self._requestor)
        self.qos = Qos(self._requestor)
        self.ratingPlan = RatingPlan(self._requestor)
        self.system = System(self._requestor)
        self.tiering = Tiering(self._requestor)
        self.usage = Usage(self._requestor)
        self.user = User(self._requestor)
        self.whitelist = Whitelist(self._requestor)
