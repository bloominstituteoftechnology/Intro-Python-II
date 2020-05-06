#!/usr/bin/env python3
# -*- coding: utf-8- 

import unittest
import zmq
import time
from zmq.utils import jsonapi as json

from room.utils.publisher import Publisher
from room.tests.utils.subscriber import Subscriber

@unittest.skip("コルーチン化しないとテストできないっぽい")
class PublisherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.publisher = Publisher('127.0.0.1:5556')
        cls.subscriber = Subscriber('127.0.0.1:5556', b'test')        
        
    def test_send(self):
        self.publisher.send('test', 'method', '{"temp": 20, "humid": 30}')
        result = self.subscriber.recv()
        self.assertEqual(result[0], b'test') # data_type
        
        msg = json.loads(result[1])
        self.assertEqual(msg[0], 'method')
        
        data = json.loads(msg[1])
        self.assertEqual(data['temp'], 20)
        self.assertEqual(data['humid'], 30)        

    @classmethod
    def tearDownClass(cls):
        cls.publisher.stop()
        cls.subscriber.stop()
        
if __name__ == '__main__':
    unittest.main()        
        
