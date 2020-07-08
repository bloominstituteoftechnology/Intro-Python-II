#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import json

from room.mining.naive_cf_data import NaiveCFData

@unittest.skip("TODO")
class NaiveCFDataTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.naive_cf_data = NaiveCFData()

    def setUp(self):
        data = json.loads('{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349068860000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.1612054489, "humidity": 0.1882105153, "out_brightness": -0.2450407919, "out_humidity": 0.1086926153, "out_pressure": 0.0142628603, "out_temperature": 0.0239133782, "people": -0.1040588553, "temperature": 0.1238222059, "timestamp": 1349068860000, "w_humidity": 0.1882098846, "w_light": -0.1504021764, "w_sound": -0.0020367455, "w_temperature_c": 0.112190812, "w_temperature_f": 0.0762658346}, "timestamp": "2015-11-11 17:33:02.958697+09:00"}')
        self.naive_cf_data.add(data)

    def test_all(self):
        result = self.naive_cf_data.all()

    def test_add(self):
        data = json.loads('{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349068860000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.1612054489, "humidity": 0.1882105153, "out_brightness": -0.2450407919, "out_humidity": 0.1086926153, "out_pressure": 0.0142628603, "out_temperature": 0.0239133782, "people": -0.1040588553, "temperature": 0.1238222059, "timestamp": 1349068860000, "w_humidity": 0.1882098846, "w_light": -0.1504021764, "w_sound": -0.0020367455, "w_temperature_c": 0.112190812, "w_temperature_f": 0.0762658346}, "timestamp": "2015-11-11 17:33:02.958697+09:00"}')
        self.naive_cf_data.add(data)
        
    def test_sensors(self):
        result = self.naive_cf_data.sensors()
        
    def test_appliances(self):
        result = self.naive_cf_data.appliances()
        
    def test_set(self):
        result = self.naive_cf_data.set()

    def tearDown(self):
        self.naive_cf_data.drop()
        
    @classmethod
    def tearDownClass(cls):
        cls.naive_cf_data.drop()        
        
if __name__ == '__main__':
    unittest.main()
