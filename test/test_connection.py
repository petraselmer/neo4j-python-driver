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


from neo4j.v1.bolt import ConnectionPool

from test.util import ServerTestCase


class QuickConnection(object):

    closed = False
    defunct = False

    def __init__(self, socket):
        self.socket = socket
        self.address = socket.getpeername()

    def reset(self):
        pass

    def close(self):
        self.socket.close()


def connector(address):
    from socket import create_connection
    return QuickConnection(create_connection(address))


def assert_pool_size(pool, address, expected_active, expected_inactive):
    try:
        connections = pool._connections[address]
    except KeyError:
        assert 0 == expected_active
        assert 0 == expected_inactive
    else:
        assert len([c for c in connections if c.in_use]) == expected_active
        assert len([c for c in connections if not c.in_use]) == expected_inactive


class ConnectionPoolTestCase(ServerTestCase):

    def test_can_acquire(self):
        with ConnectionPool(connector) as pool:
            address = ("127.0.0.1", 7687)
            connection = pool.acquire(address)
            assert connection.address == address
            assert_pool_size(pool, address, 1, 0)

    def test_can_acquire_twice(self):
        with ConnectionPool(connector) as pool:
            address = ("127.0.0.1", 7687)
            connection_1 = pool.acquire(address)
            connection_2 = pool.acquire(address)
            assert connection_1.address == address
            assert connection_2.address == address
            assert connection_1 is not connection_2
            assert_pool_size(pool, address, 2, 0)

    def test_can_acquire_two_addresses(self):
        with ConnectionPool(connector) as pool:
            address_1 = ("127.0.0.1", 7687)
            address_2 = ("127.0.0.1", 7474)
            connection_1 = pool.acquire(address_1)
            connection_2 = pool.acquire(address_2)
            assert connection_1.address == address_1
            assert connection_2.address == address_2
            assert_pool_size(pool, address_1, 1, 0)
            assert_pool_size(pool, address_2, 1, 0)

    def test_can_acquire_and_release(self):
        with ConnectionPool(connector) as pool:
            address = ("127.0.0.1", 7687)
            connection = pool.acquire(address)
            assert_pool_size(pool, address, 1, 0)
            pool.release(connection)
            assert_pool_size(pool, address, 0, 1)

    def test_releasing_twice(self):
        with ConnectionPool(connector) as pool:
            address = ("127.0.0.1", 7687)
            connection = pool.acquire(address)
            pool.release(connection)
            assert_pool_size(pool, address, 0, 1)
            pool.release(connection)
            assert_pool_size(pool, address, 0, 1)
