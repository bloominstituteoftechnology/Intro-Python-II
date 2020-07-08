#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import json
import datetime
from room.database.mongo import MongoDB

class MongoDBTest(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        cls.mongo = MongoDB()

    def test_save(self):
        data = (b'', '{"appliances": {"CeilingLight1": 0.0, "CeilingLight2": 0.0, "CeilingLight3": 0.0, "airCleaner": 0.0, "airConditioner": 0.0, "airConditionerFront": 0.0, "aircleaner001": 0.0, "aircon001": 0.0, "allLight": 0.0, "allLight001": 0.0, "aroma": 0.0, "aroma001": 0.0, "dvd001": 0.0, "fan": 0.0, "fan001": 0.0, "floorLight": 0.0, "floorLight001": 0.0, "frontCeilingLight": 0.0, "hddJukeBox": 0.0, "hddRecorder": 0.0, "hotCarpet001": 0.0, "newAirCleaner": 0.0, "speaker002": 0.0, "tableLight": 0.0, "tableLight001": 0.0, "timestamp": 1349053560000, "tv": 0.0, "tv001": 0.0, "viera": 0.0, "windAirCon001": 0.0}, "sensors": {"airflow": -0.133715697, "brightness": -0.3495616132, "humidity": 0.1882105153, "out_brightness": -0.248049819, "out_humidity": 0.0966444225, "out_pressure": 0.0096008556, "out_temperature": 0.0286677364, "people": -0.1665588553, "temperature": 0.1238222059, "timestamp": 1349053560000, "w_humidity": 0.1882098846, "w_light": -0.4184434136, "w_sound": -0.0020367455, "w_temperature_c": 0.1074010302, "w_temperature_f": 0.0730542729}, "timestamp": "2015-11-16 22:47:31.285455+09:00"}')
        post = json.loads(data[1])
        self.mongo.save(post)
        
    def test_load(self):
        post = {"author": "Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}
        self.mongo.save(post)
        result = self.mongo.load()
        self.assertEqual(result[0]['author'], "Mike")
        self.assertEqual(result[0]['text'], "My first blog post!")


    @classmethod
    def tearDownClass(cls):
        cls.mongo.drop()

    
if __name__ == '__main__':
    unittest.main()
