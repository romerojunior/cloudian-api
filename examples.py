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


from cloudianapi.client import CloudianAPIClient

if __name__ == "__main__":

    client = CloudianAPIClient(
        url="https://your-company",
        user="username",
        key="password",
        port=8080
    )

    # Parameters such as nodeId, region, userType and so on are case sensitive,
    # check your Cloudian (TM) Admin API documentation for more details.

    # Print dict containing all nodes:
    print client.monitor.nodelist()

    # Print details about a given node:
    print client.monitor.host(nodeId="node01")

    # Print all events of a given node from a specific region:
    print client.monitor.events(nodeId="node01", region="eu-west-1")

    # Print notification rules for a given region:
    print client.monitor.notificationrules(region="eu-west-1")

    # Print license details:
    print client.system.license()

    # Print details about a given group:
    print client.group(groupId="ABC")

    # Print a list of active users from a given user group:
    print client.user.list(groupId="ABC", userType="all", userStatus="active")

    # Print all nodes from a given region and their respective used capacity:
    for node in client.monitor.nodelist(region="eu-west-1"):
        print '{node}: {value} KB used'.format(
            value=client.monitor.host(nodeId=node)['diskUsedKb']['value'],
            node=node
        )

    # Deleting user Cartman from a given group:
    print client.user(method="DELETE", userId="Cartman", groupId="ABC")

    # Adding user Butters to a given group:
    payload = {
        "userId": "Butters",
        "groupId": "ABC",
        "userType": "User"
    }

    print client.user(method='PUT', json=payload)
