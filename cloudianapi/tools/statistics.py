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

from numpy import median, mean


def mean_disk_deviation(node_monitor):
    """ Gets the monitoring output of a given node and returns the deviation on
    storage usage for each disk.

    :param node_monitor:    an iterable object
    :type node_monitor:     dict
    :rtype:                 int
    """

    ft = (lambda x: True if 'HS' in x['storageUse'] else False)

    hs_disks = filter(
        ft, (disk for disk in node_monitor['disksInfo']['disks'])
    )

    hs_usage = [abs(int(disk['diskUsedKb'])) for disk in hs_disks]

    m = int(median(hs_usage))

    deviation = [abs(kb_used - m) for kb_used in hs_usage]

    return int(mean(deviation))
