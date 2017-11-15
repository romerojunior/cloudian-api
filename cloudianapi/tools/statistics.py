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

""" This is not part of the Admin API, but it incorporates additional tooling
to support statistical analysis of monitored data within a cluster, data center
or node """


def get_hs_used_kb(node):
    """ Receives a node monitor JSON string and returns a list containing the
    used disk space in KB for each hyperstore disk.

    :param node:            an iterable object
    :type node:             dict
    :rtype:                 list
    """

    if 'disksInfo' not in node:
        raise TypeError('Unsupported input.')

    # filter function to select only HyperStore disks:
    f = (lambda n: True if 'HS' in n['storageUse'] else False)

    hs_disks = filter(
        f, (d for d in node['disksInfo']['disks'])
    )

    return [abs(int(disk['diskUsedKb'])) for disk in hs_disks]


def disk_avg_abs_deviation(node):
    """ Returns the average absolute deviation for a given set of disks of a
    given node based entirely on used capacity (expressed in KB).

    Particularly useful if you want to visualize the average difference
    between all disks in a given node. The closer the result is to zero the
    better (less deviation = balanced usage).

    :param node:            an iterable object
    :type node:             dict
    :rtype:                 int
    """
    try:
        disk_usage = get_hs_used_kb(node)
    except TypeError:
        return 0

    mean = (sum(disk_usage) / len(disk_usage))

    deviation = [abs(kb_used - mean) for kb_used in disk_usage]

    return sum(deviation)/len(deviation)
