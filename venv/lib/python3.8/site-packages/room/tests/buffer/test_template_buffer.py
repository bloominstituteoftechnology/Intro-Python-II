#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from zmq.utils import jsonapi as json

from room.buffer.template_buffer import TemplateBufferModule, TemlateStateHandler
from room.tests.utils.subscriber import Subscriber

@unittest.skip("TODO")
class TemlateStateHandlerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.state_handler = TemlateStateHandler()
        cls.subscriber = Subscriber('127.0.0.1:5550')

    @unittest.skip('parseエラー')
    def test_update_sensor(self):
        self.state_handler.update_sensor(data)
        data = {'test_temperature': 22}
        result = self.state_handler.get_sensor()
        self.assertEqual(result['test_temperature'], 22)

    @unittest.skip('parseエラー')        
    def test_update_appliance(self):
        data = {'viera': 1}
        self.state_handler.update_appliance(data)
        result = self.state_handler.get_appliance()
        self.assertEqual(result['viera'], 1)

    @unittest.skip("コルーチン化しないとテストできないっぽい")        
    def test_call(self):
        self.state_handler.update_sensor({'test_temperature': 22})
        self.state_handler.update_appliance({'viera': 1})        
        self.state_handler.__call__()

        result = self.subscriber.recv()
        
        msg = json.loads(result[1])
        self.assertEqual(msg[0], 'mining')
        
        data = json.loads(msg[1])
        self.assertEqual(data['sensors']['test_temperature'], 22)                
        self.assertEqual(data['appliances']['viera'], 1)

    @classmethod
    def tearDownClass(cls):
        cls.subscriber.stop()
        
if __name__ == '__main__':
    unittest.main()
        
