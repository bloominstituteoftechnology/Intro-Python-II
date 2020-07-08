#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from datetime import datetime
from dateutil.parser import parse 

from room.utils.log import logging

class CBR(object):
    '''
    事例ベース推論

    '''

    def __init__(self):
        self.sensor_stat = {}


    def update_sensor_stat(self, sensor, current_val):
        '''
        '''
        if sensor not in self.sensor_stat: # 初めてあらわれたセンサなら
            self.sensor_stat[sensor] = {}
            self.sensor_stat[sensor]['min'] = current_val
            self.sensor_stat[sensor]['max'] = current_val
        elif current_val > self.sensor_stat[sensor]['max']: # センサ値が過去最高なら
            self.sensor_stat[sensor]['max'] = current_val
        elif current_val < self.sensor_stat[sensor]['min']: # センサ値が過去最低なら
            self.sensor_stat[sensor]['min'] = current_val
        else:
            pass
            
    def attribute_dist(self, sensor, current_val, record_val):
        '''

        '''
        self.update_sensor_stat(sensor, current_val) # 最大値・最小値更新
        max_dis = self.sensor_stat[sensor]['max'] - self.sensor_stat[sensor]['min']
        if max_dis == 0: return 0

        return math.fabs(current_val - record_val) / max_dis
                        

        
    
    def sensor_dist(self, current, record):
        '''

        '''
        sensors = current.keys()
        sensor_num = len(sensors)
        if sensor_num == 0: return 1 # ガード節
        
        dist_sum = 0
        for sensor in sensors:
            if sensor in record:
                dist_sum += self.attribute_dist(sensor, current[sensor], record[sensor])
            else:
                dist_sum += 1 # センサ値がなかった場合 厳しすぎるかも？

        return dist_sum / sensor_num
        
        
    def inout_dist(self, current, record):

        total_people_num = len(current.keys())
        if total_people_num == 0: return 1 # inout情報がない場合は完全に異なっているとして扱う
        
        dist = 0
        for user in current:
            if user in record and current[user] == record[user]:
                pass
            else:
                dist += 1

        return dist / total_people_num
        

    
    def time_dist(self, timestamp1, timestamp2):
        '''
        時間の類似度を計算する

        '''
        # weights
        day_w = 0.2
        week_w = 0.4
        minute_w = 0.4
        
        d1 = parse(timestamp1)
        d2 = parse(timestamp2)

        week_dist = math.fabs(d1.weekday() - d2.weekday()) / 7
        minute_dist = math.fabs(self.elapsed_minute(d1) - self.elapsed_minute(d2)) / (60 * 24)
        day_dist = math.fabs(self.elapsed_day(d1) - self.elapsed_day(d2)) / 365

        return day_w * day_dist + week_w * week_dist + minute_w * minute_dist

    def elapsed_minute(self, d):
        '''
        その日の0時0分からの経過分数を返す

        '''
        return d.time().hour * 60 + d.time().minute

    def elapsed_day(self, d):
        '''
        その日の1月1日からの経過日数を返す

        '''
        diff = d.date() - datetime(d.date().year, 1, 1).date()        
        return diff.days

    
    def global_similarity(self, current, record):
        '''
        ex: {'tmp': 20, 'hum': 10, 'takatori': 3, 'timestamp': ''}

        '''
        # sensor_w + tim_w + inout_w = 1
        sensor_w = 0.4
        time_w = 0.4
        inout_w = 0.2
        
        sensor_dist = self.sensor_dist(current['sensors'], record['sensors']) # 0 ~ 1
        time_dist = self.time_dist(current['timestamp'], record['timestamp']) # 0 ~ 1
        inout_dist = self.inout_dist(current['inout'], record['inout']) # 0 ~ 1
        
        return 1 - (sensor_w * sensor_dist + time_w * time_dist + inout_w * inout_dist)

        
    def prediction(self, current, records):

        result = {}
        appliances = current['appliances'].keys() # 現在の家電の種類
        sim_sum = 0 # 類似度の合計
        
        for record in records: # 全ての過去のレコードに対して
            sim = self.global_similarity(current, record) # 類似度計算

            for appliance in appliances: # 各家電に対して
                if appliance not in result: result[appliance] = 0
                if appliance in record['appliances']: # レコードに存在していれば
                    result[appliance] += sim * record['appliances'][appliance]
                    sim_sum += sim
                    
        return [(r[0], r[1] / sim_sum) for r in result.items()] # 正規化


    def recommend(self, current, records, on_threshold=0.8, off_threshold=0.2):

        predictions = self.prediction(current, records)
        logging.info(str(predictions))
        result = []

        for appliance, score in predictions:
            current_state = current['appliances'][appliance]
            if current_state == 0 and score >= on_threshold:
                result.append({'appliance':appliance, 'method':1}) # onのレコメンド
            elif current_state == 1 and score <= off_threshold:
                result.append({'appliance':appliance, 'method':0}) # offのレコメンド

        return result
                
if __name__ == "__main__":
    
    current = {
        "appliances": {
            "ceilinglight": 0,
            "aircon": 0,
            "fan": 0,
            "curtain": 0,
            "viera": 0,
            "floorlight": 0
        },
        "inout": {
            "sakaki": 0,
            "tamamizu": 0,            
            "inomoto": 0,
            "sachio": 0,
            "junho": 0,
            "tktk": 0,
            "takatori": 1,
            "horihori": 0,
            "otokunaga": 1,
            "tabata": 0,
            "masa-n": 0,
            "usk108": 0,
            "longniu": 0,
            "masuda": 0,
            "shinsuke": 0,
            "arisa": 0            
        },
        "sensors": {
            "core01_brightness": 34.848484,
            "core01_pir count": 0,
            "core04_brightness": 0,
            "core04_pir count": 0,
            "core01_temperature": 26.299999,
            "core04_temperature": 0,
            "core04_humidity": 0,
            "core01_pressure": 1004.775635,
            "core02_pressure": 998.34137,
            "core02_humidity": 23.700001,
            "core01_humidity": 17.4,
            "core02_temperature": 26,
            "core04_pressure": 0,
            "core02_brightness": 28.787878,
            "core02_pir count": 21,
        },
        "timestamp": "2016-01-08 22:08:50.970682+09:00"
    }

    record1 = {
        "appliances": {
            "ceilinglight": 0,
            "aircon": 0,
            "fan": 0,
            "curtain": 1,
            "viera": 0,
            "floorlight": 0
        },
        "inout": {
            "sakaki": 1,
            "tamamizu": 0,            
            "inomoto": 0,
            "sachio": 0,
            "junho": 0,
            "tktk": 0,
            "takatori": 1,
            "horihori": 1,
            "otokunaga": 1,
            "tabata": 0,
            "masa-n": 0,
            "usk108": 1,
            "longniu": 0,
            "masuda": 0,
            "shinsuke": 0,
            "arisa": 0            
        },
        "sensors": {
            "core01_temperature": 27.799999,
            "core01_brightness": 28.787878,
            "core01_pir count": 0,
            "core02_brightness": 12.121212,
            "core01_humidity": 24.6,
            "core04_pressure": 1018.481323,
            "core04_humidity": 31.4,
            "core02_pir count": 1,
            "core04_temperature": 25.1,
            "core02_humidity": 29.799999,
            "core02_temperature": 24.5,
            "core02_pressure": 1014.526245,
            "core04_pir count": 0,
            "core01_pressure": 1016.13501,
            "core04_brightness": 480.30304
        },
        "timestamp": "2016-01-08 20:08:50.970682+09:00"
    }
    
    record2 = {
        "appliances": {
            "ceilinglight": 1,
            "aircon": 0,
            "fan": 0,
            "curtain": 1,
            "viera": 0,
            "floorlight": 0
        },
        "inout": {
            "sakaki": 1,
            "tamamizu": 0,            
            "inomoto": 0,
            "sachio": 0,
            "junho": 0,
            "tktk": 0,
            "takatori": 1,
            "horihori": 1,
            "otokunaga": 1,
            "tabata": 0,
            "masa-n": 0,
            "usk108": 1,
            "longniu": 0,
            "masuda": 0,
            "shinsuke": 0,
            "arisa": 0            
        },
        "sensors": {
            "core01_temperature": 20.799999,
            "core01_brightness": 29.787878,
            "core01_pir count": 0,
            "core02_brightness": 13.121212,
            "core01_humidity": 24.6,
            "core04_pressure": 1018.481323,
            "core04_humidity": 31.4,
            "core02_pir count": 1,
            "core04_temperature": 25.1,
            "core02_humidity": 29.799999,
            "core02_temperature": 24.3,
            "core02_pressure": 1014.526245,
            "core04_pir count": 0,
            "core01_pressure": 1016.13501,
            "core04_brightness": 480.30304
        },
        "timestamp": "2016-01-08 22:08:50.970682+09:00"
    }
    
    
    records = [record1, record2]


    cbr = CBR()
    print(cbr.prediction(current, records))
    print(cbr.recommend(current, records))
    
