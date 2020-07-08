#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import json

from room.utils import converter

@unittest.skip("TODO")
class ConverterTest(unittest.TestCase):

    def test_dict_to_df(self):
        data = json.loads('{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349068860000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.1375886637, "brightness": -0.1612054489, "humidity": 0.1882105153, "out_brightness": -0.2450407919, "out_humidity": 0.1086926153, "out_pressure": 0.0142628603, "out_temperature": 0.0239133782, "people": -0.1040588553, "temperature": 0.1238222059, "timestamp": 1349068860000, "w_humidity": 0.1882098846, "w_light": -0.1504021764, "w_sound": -0.0020367455, "w_temperature_c": 0.112190812, "w_temperature_f": 0.0762658346}, "timestamp": "2015-11-11 17:33:02.958697+09:00"}')
        result = converter.dict_to_df(data)


if __name__ == '__main__':
    unittest.main()
    
