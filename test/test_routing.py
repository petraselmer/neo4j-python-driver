#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2016 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# from os.path import join as join_path, normpath
# from subprocess import check_call
# from unittest import TestCase
#
# from neo4j.v1 import basic_auth, GraphDatabase, RoutingDriver
# from os.path import dirname
#
# TEST = normpath(dirname(__file__))
# TEST_RESOURCES = join_path(TEST, "resources")
# BOLT_ROUTING_URI = "bolt+routing://127.0.0.1:9001"
# AUTH_TOKEN = basic_auth("neotest", "neotest")
#
#
# class RoutingTestCase(TestCase):
#
#     def setUp(self):
#         check_call(["boltstub", "9001", join_path(TEST_RESOURCES, "discover_servers.script")])
#
#     def test_should_do_routing_on_initialization(self):
#         with GraphDatabase.driver(BOLT_ROUTING_URI, auth=AUTH_TOKEN) as driver:
#             assert isinstance(driver, RoutingDriver)
