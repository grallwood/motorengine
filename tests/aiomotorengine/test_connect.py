#!/usr/bin/env python

import sys

from preggy import expect
import asyncio

from motorengine.aiomotorengine import connect
from motorengine.connection import (
    ConnectionError, get_motor_client_classes, get_database_class
)
from tests.aiomotorengine import AsyncTestCase, async_test


class TestConnect(AsyncTestCase):
    def setUp(self):
        super(TestConnect, self).setUp(auto_connect=False)

    def test_get_motor_client_classes(self):
        from motor.motor_tornado import MotorClient
        from motor.motor_asyncio import AsyncIOMotorClient

        client = get_motor_client_classes()
        expect(client).to_equal(MotorClient)

        client = get_motor_client_classes(framework='tornado')
        expect(client).to_equal(MotorClient)

        client = get_motor_client_classes(framework='asyncio')
        expect(client).to_equal(AsyncIOMotorClient)

    def test_get_database_class(self):
        Database = get_database_class()
        import motorengine.database
        expect(Database).to_equal(motorengine.database.Database)

        Database = get_database_class(framework='tornado')
        expect(Database).to_equal(motorengine.database.Database)

        Database = get_database_class(framework='asyncio')
        import motorengine.aiomotorengine.database
        expect(Database).to_equal(motorengine.aiomotorengine.database.Database)

    @async_test
    @asyncio.coroutine
    def test_can_connect_to_a_database(self):
        db = connect('test', host="localhost", port=27017,
                     io_loop=self.io_loop)

        res = yield from db.ping()
        ping_result = res['ok']
        expect(ping_result).to_equal(1.0)

    @async_test
    @asyncio.coroutine
    def test_connect_to_replica_set(self):
        db = connect('test', host="localhost:27017,localhost:27018",
                     replicaSet="rs0", port=27018, io_loop=self.io_loop)

        res = yield from db.ping()
        ping_result = res['ok']
        expect(ping_result).to_equal(1.0)
