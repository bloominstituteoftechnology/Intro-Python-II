#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime
import pytz

class State:
    '''
    センサや家電の状態を保持するクラス

    '''
    def __init__(self):
        self._sensor_state = {} # sensorの状態を保持する辞書
        self._inout_state = {} # 入退室の状態を保持する辞書
        self._applianece_state = {} # applianceの状態を保持する辞書
        
    def __str__(self):
        return str(self.dump_at_now())

    def format_sensors(self, keys, value):
        for key in keys:
            self._sensor_state[key] = value

    def format_appliances(self, keys,value):
        for key in keys:
            self._applianece_state[key] = value

    def format_inout(self, keys, value):
        for key in keys:
            self._inout_state[key] = value

    def update_sensor(self, key, value):
        '''
        sensorの状態を更新する

        '''
        self._sensor_state[key] = value

    def update_inout(self, key, value):
        '''
        入退室の状態を更新する

        '''
        self._inout_state[key] = value

    def update_appliance(self, key, value):
        '''
        applianceの状態を更新する

        '''        
        self._applianece_state[key] = value

    def get_sensor_keys(self):
        '''
        sensorの種類を取得する

        @return dict_keys
        '''
        return self._sensor_state.keys()


    def get_inout_keys(self):
        return self._inout_state.keys()
    

    def get_appliance_keys(self):
        '''
        applianceの種類を取得する

        @return dict_keys
        '''        
        return self._applianece_state.keys()

    def get_sensor_value(self, key):
        return self._sensor_state[key]


    def get_inout_value(self, key):
        return self._inout_state[key]
    

    def get_appliance_value(self, key):
        return self._applianece_state[key]
    
    def dump(self):
        '''
        sensor, applianceの状態を辞書にして返す

        @return dict
        '''                
        return {"sensors": self._sensor_state, "inout": self._inout_state, "appliances": self._applianece_state}


    def dump_with_timestamp(self, time):
        '''
        timestampを付与して辞書で返す

        @return dict
        '''
        return {"timestamp": str(time), "sensors": self._sensor_state, "inout": self._inout_state, "appliances": self._applianece_state}


    def dump_at_now(self):
        '''
        現在の時刻をタイムスタンプとして辞書を返す

        @return dict
        '''
        tz = pytz.timezone('Asia/Tokyo')
        now = datetime.now(tz)
        return self.dump_with_timestamp(now)
    
