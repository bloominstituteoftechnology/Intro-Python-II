#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import json

from room.mining.naive_cf import NaiveCollaborativeFiltering

@unittest.skip("TODO")
class NaiveCollaborativeFilteringTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.naive_cf = NaiveCollaborativeFiltering()
        data = json.loads('{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349068860000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.1612054489, "humidity": 0.1882105153, "out_brightness": -0.2450407919, "out_humidity": 0.1086926153, "out_pressure": 0.0142628603, "out_temperature": 0.0239133782, "people": -0.1040588553, "temperature": 0.1238222059, "timestamp": 1349068860000, "w_humidity": 0.1882098846, "w_light": -0.1504021764, "w_sound": -0.0020367455, "w_temperature_c": 0.112190812, "w_temperature_f": 0.0762658346}, "timestamp": "2015-11-11 17:33:02.958697+09:00"}')        
        cls.naive_cf._data.add(data)
        data = json.loads('{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349223120000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.3495616132, "humidity": 0.0715438486, "out_brightness": -0.248049819, "out_humidity": 0.0022669125, "out_pressure": 0.0142628603, "out_temperature": 0.0334220946, "people": -0.1040588553, "temperature": 0.1238222059, "timestamp": 1349223120000, "w_humidity": 0.071543218, "w_light": -0.4184434136, "w_sound": -0.0020367455, "w_temperature_c": 0.113255208, "w_temperature_f": 0.0769683637}, "timestamp": "2015-11-12 15:42:02.960944+09:00"}')        
        cls.naive_cf._data.add(data)
        data = json.loads('{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349222760000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.3495616132, "humidity": 0.0715438486, "out_brightness": -0.248049819, "out_humidity": -0.0077732482, "out_pressure": 0.0165938626, "out_temperature": 0.0334220946, "people": -0.1040588553, "temperature": 0.1178342626, "timestamp": 1349222760000, "w_humidity": 0.071543218, "w_light": -0.4184434136, "w_sound": -0.0020367455, "w_temperature_c": 0.1153839999, "w_temperature_f": 0.0784737832}, "timestamp": "2015-11-12 15:41:02.960992+09:00"}')        
        cls.naive_cf._data.add(data)
        data = json.loads('{"appliances": {"CeilingLight1": 1.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349222400000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.3495616132, "humidity": 0.0715438486, "out_brightness": -0.248049819, "out_humidity": -0.0097812803, "out_pressure": 0.0142628603, "out_temperature": 0.0350068806, "people": -0.1040588553, "temperature": 0.1178342626, "timestamp": 1349222400000, "w_humidity": 0.071543218, "w_light": -0.4184434136, "w_sound": -0.0020367455, "w_temperature_c": 0.1183110888, "w_temperature_f": 0.0803806479}, "timestamp": "2015-11-12 15:40:02.958731+09:00"}')
        cls.naive_cf._data.add(data)
        
    def test_mining(self):
        data = json.loads('{"appliances": {"CeilingLight1": 1.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349222400000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.3495616132, "humidity": 0.0715438486, "out_brightness": -0.248049819, "out_humidity": -0.0097812803, "out_pressure": 0.0142628603, "out_temperature": 0.0350068806, "people": -0.1040588553, "temperature": 0.1178342626, "timestamp": 1349222400000, "w_humidity": 0.071543218, "w_light": -0.4184434136, "w_sound": -0.0020367455, "w_temperature_c": 0.1183110888, "w_temperature_f": 0.0803806479}, "timestamp": "2015-11-12 15:40:02.958741+09:00"}')        
        result = self.naive_cf.mining(data)
        print('result {0}'.format(str(result)))
        
    def test_predict(self):
        self.assertTrue(True)

    def test_recommend(self):
        self.assertTrue(True)
        
    @classmethod
    def tearDownClass(cls):
        'todo'

if __name__ == '__main__':
    unittest.main()
        
