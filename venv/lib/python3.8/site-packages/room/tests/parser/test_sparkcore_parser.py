#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json

from room.parser.sparkcore_parser import SparkCoreParserModule, SparkCoreParser
from room.utils.publisher import Publisher
from room.tests.utils.subscriber import Subscriber

@unittest.skip("コルーチン化しないとテストできないっぽい")
class SparkCoreParserModuleTest(unittest.TestCase)            :

    @classmethod
    def setUpClass(cls):
        cls.publisher = Publisher("127.0.0.1:5558")
        cls.sparkcore_parser = SparkCoreParserModule("127.0.0.1:5558")
        cls.sparkcore_parser.run()
        cls.subscriber = Subscriber('127.0.0.1:5557')

    def test_sparkcore_parser_module(self):

        data = """
        ["sparkcore",{
        "sensorId": "core04",
        "temperature": 27.6,
        "humidity": 41.200001,
        "pressure": 991.455566,
        "brightness": 34.848484,
        "pir_count": 0
        }]"""

        self.publisher().send('sparkcore', 'parse', data)
        result = self.subscribe.recv()
        print(result)
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        print('tearDown!!!') 
        cls.sparkcore_parser.stop()        
        
class SparkCoreParserTest(unittest.TestCase):

    def test_parser(self):
        parser = SparkCoreParser()
        data = """
        ["sparkcore",{
        "sensorId": "core04",
        "temperature": 27.6,
        "humidity": 41.200001,
        "pressure": 991.455566,
        "brightness": 34.848484,
        "pir_count": 0
        }]"""
        results = parser.parse(json.loads(data))
        expections = ['{"core04_temperature": 27.6}',
                      '{"core04_humidity": 41.200001}',
                      '{"core04_pressure": 991.455566}',
                      '{"core04_brightness": 34.848484}',
                      '{"core04_pir_count": 0}']
        for result in results:
            self.assertEqual(result[0], 'sensor')
            self.assertTrue(result[1] in expections)


        
if __name__ == '__main__':
    unittest.main()        

