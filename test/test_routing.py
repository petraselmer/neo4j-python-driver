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
from unittest import TestCase

from neo4j.v1 import basic_auth, GraphDatabase, RoutingDriver, READ_ACCESS


# from os.path import dirname

# TEST = normpath(dirname(__file__))
# TEST_RESOURCES = join_path(TEST, "resources")
# BOLT_ROUTING_URI = "bolt+routing://127.0.0.1:9001"
# AUTH_TOKEN = basic_auth("neotest", "neotest")


class LocalClusterIntegrationTestCase(TestCase):

    def test_should_be_able_to_run_cypher(self):
        uri = "bolt+routing://ec2-54-78-203-70.eu-west-1.compute.amazonaws.com:26000"
        driver = GraphDatabase.driver(uri, auth=basic_auth("neo4j", "password"))
        try:
            with driver.session(READ_ACCESS) as session:
                result = session.run("UNWIND range(1, 3) AS n RETURN n")
                for record in result:
                    print(record)
                print(result.summary.metadata)
                print(session.connection.address)
        finally:
            driver.close()

    def test_should_discover_servers_on_driver_construction(self):
        uri = "bolt+routing://ec2-54-78-203-70.eu-west-1.compute.amazonaws.com:26000"
        driver = GraphDatabase.driver(uri, auth=basic_auth("neo4j", "password"))
        print(driver._routers)
        print(driver._readers)
        print(driver._writers)
