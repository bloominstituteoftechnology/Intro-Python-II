#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import pytz
from datetime import datetime
from room.buffer.state import State

class StateTest(unittest.TestCase):

    def test_get_sensor_keys(self):
        state = State()        
        state.update_sensor('temp', 22)
        state.update_sensor('humid', 23)
        state.update_sensor('pressure', 23)   
        self.assertEqual(len(state.get_sensor_keys()), 3)
        self.assertTrue('temp' in list(state.get_sensor_keys()))
        self.assertTrue('humid' in list(state.get_sensor_keys()))
        self.assertTrue('pressure' in list(state.get_sensor_keys()))
        
    def test_get_appliance_keys(self):
        state = State()        
        state.update_appliance('tv', 1)
        state.update_appliance('tv', 0)
        state.update_appliance('light', 1)                       
        self.assertEqual(len(state.get_appliance_keys()), 2)
        self.assertTrue('tv' in list(state.get_appliance_keys()))
        self.assertTrue('light' in list(state.get_appliance_keys()))
    
    def test_update_sensor(self):
        state = State()
        state.update_sensor('temp', 22)
        state.update_sensor('humid', 23)
        state.update_sensor('pressure', 23)
        self.assertEqual(state.get_sensor_value('temp'), 22)
        self.assertEqual(state.get_sensor_value('humid'), 23)
        self.assertEqual(state.get_sensor_value('pressure'), 23)
        
    def test_update_appliance(self):
        state = State()
        state.update_appliance('tv', 1)
        state.update_appliance('tv', 0)
        state.update_appliance('light', 1)          
        self.assertEqual(len(state.get_appliance_keys()), 2)
        self.assertEqual(state.get_appliance_value('tv'), 0)
        self.assertEqual(state.get_appliance_value('light'), 1)
        

    def test_to_json(self):
        state = State()
        state.update_sensor('temp', 22)
        state.update_sensor('humid', 23)
        state.update_sensor('pressure', 23)
        state.update_appliance('tv', 1)
        state.update_appliance('tv', 0)
        state.update_appliance('light', 1)                  
        result = state.to_json()
        self.assertTrue(isinstance(result, str))
        result = json.loads(result)
        self.assertEqual(result['sensors']['temp'], 22)
        self.assertEqual(result['sensors']['humid'], 23)
        self.assertEqual(result['sensors']['pressure'], 23)
        self.assertEqual(result['appliances']['tv'], 0)
        self.assertEqual(result['appliances']['light'], 1)
        
    def test_to_json_withn_timestamp(self):
        state = State()
        state.update_sensor('temp', 22)
        state.update_sensor('humid', 23)
        state.update_sensor('pressure', 23)
        state.update_appliance('tv', 1)
        state.update_appliance('tv', 0)
        state.update_appliance('light', 1)
        tz = pytz.timezone('Asia/Tokyo')
        now = datetime.now(tz)        
        result = state.to_json_with_timestamp(now)
        self.assertTrue(isinstance(result, str))
        result = json.loads(result)
        self.assertEqual(result['timestamp'], str(now))
        self.assertEqual(result['sensors']['temp'], 22)
        self.assertEqual(result['sensors']['humid'], 23)
        self.assertEqual(result['sensors']['pressure'], 23)
        self.assertEqual(result['appliances']['tv'], 0)
        self.assertEqual(result['appliances']['light'], 1)


    def test_to_json_at_now(self):
        state = State()
        state.update_sensor('temp', 22)
        state.update_sensor('humid', 23)
        state.update_sensor('pressure', 23)
        state.update_appliance('tv', 1)
        state.update_appliance('tv', 0)
        state.update_appliance('light', 1)
        tz = pytz.timezone('Asia/Tokyo')
        now = datetime.now(tz)        
        result = state.to_json_at_now()
        self.assertTrue(isinstance(result, str))
        result = json.loads(result)
        self.assertEqual(result['timestamp'].split(' ')[0], str(now).split(' ')[0]) # 年月日の一致
        self.assertEqual(result['timestamp'].split(' ')[1].split('.')[0], str(now).split(' ')[1].split('.')[0]) #時間の一致
        self.assertEqual(result['sensors']['temp'], 22)
        self.assertEqual(result['sensors']['humid'], 23)
        self.assertEqual(result['sensors']['pressure'], 23)
        self.assertEqual(result['appliances']['tv'], 0)
        self.assertEqual(result['appliances']['light'], 1)

if __name__ == '__main__':
    unittest.main()        
