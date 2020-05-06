# -*- coding: utf-8 -*-
import numpy as np
import random
from pymongo import MongoClient
from room.utils.config import config

from datetime import datetime
from dateutil.parser import parse

class Data(object):

    def __init__(self):
        self._client     = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
        self._db         = self._client[config['mongo']['db']]
        self._collection = self._db[config['mongo']['collection']]

        self.data_list = [            
            "core01_temperature",
            "core02_temperature",                        
            "core04_temperature",
            "core01_brightness",
            "core02_brightness",
            "core04_brightness",            
            "core01_humidity",
            "core02_humidity",            
            "core04_humidity",
            "core01_pressure",
            "core02_pressure",
            "core04_pressure",            
            "core01_pir count",
            "core02_pir count",
            "core04_pir count",
            "otokunaga",
            "masa-n",
            "inomoto",
            "junho",
            "tabata",
            "tamamizu",
            "sachio",
            "takatori",
            "horihori",
            "masuda",
            "longniu",
            "shinsuke",
            "usk108",
            "arisa",
            "tktk",
            "time",
            "sakaki"            
        ]

        self.target_list = [
            "ceilinglight",
            "aircon",
            "curtain",
            "fan",
            "floorlight",
            "viera"            
        ]

    def load_data(self, appliance, num=None):

        data = []
        target = []
        
        for record in self._collection.find()[:num]:
            sensors = record['sensors'] 
            inout   = record['inout']
            sensors.update(inout) # 2つのdictを結合
            d = [sensors[x] if x in sensors else 0 for x in self.data_list] # data_listの順にvalueを取り出し
            date = parse(record['timestamp']) 
            week = date.weekday() # 日付
            elapsed_minute = date.time().hour * 60 + date.time().minute # 0時0分からの経過分数
            d = d + [week, elapsed_minute] # data配列に追加
            t = record['appliances'][appliance]
            data.append(d)
            target.append(t)

        cs27 = {}
        cs27['data'] = np.array(data).astype(np.float32)
        cs27['target'] = np.array(target).astype(np.int32)

        return cs27
        
    def load(self, appliance, num=None):
        cs27 = {}
        data_on = [] # 説明変数 入退室・センサ targetがonの場合
        data_off = [] # 説明変数 入退室・センサ targetがoffの場合       
        on_count = 0
        off_count = 0
        
        for record in self._collection.find()[:num]: # fetch from mongodb [:None] == [:]

            sensors = record['sensors'] 
            inout   = record['inout']
            sensors.update(inout) # 2つのdictを結合
            d = [sensors[x] if x in sensors else 0 for x in self.data_list] # data_listの順にvalueを取り出し

            date = parse(record['timestamp']) 
            week = date.weekday() # 日付
            elapsed_minute = date.time().hour * 60 + date.time().minute # 0時0分からの経過分数
            d = d + [week, elapsed_minute] # data配列に追加

            t = 1 if appliance in record['appliances'] and record['appliances'][appliance] == 1 else 0  # 家電が存在していれば1それ以外は0

            if t == 1:
                on_count += 1
                data_on.append(d)                
            elif t == 0:
                off_count += 1
                data_off.append(d)                

        print('on:{0}, off:{1}'.format(on_count, off_count))
        # onの方が圧倒的に少ないのでインバランスを解消する必要がある
        # onとoffのデータ数を同じにする
        perm = np.random.permutation(off_count) # 0からoff_countまでの数字をrandomに並べた配列を返す

        data = []
        
        for i in range(0, off_count): # オーバーサンプリング onを増やす
            data.append(data_on[i % on_count])

        data = np.array(data)  # numpy arrayに変換
        data_off = np.array(data_off)  # numpy arrayに変換
        
        data = np.r_[data, data_off] # onとoffのデータ数を合わせる。offのデータはrandomに取得
        target = np.array([1] * off_count + [0] * off_count) # dataは前半がonで後半がoffになっているので、教師データをそのように作成する

        perm = np.random.permutation(off_count * 2) # ランダムに並び替え
        data = data[perm] 
        target = target[perm] 
        
        cs27['data'] = np.array(data)
        cs27['target'] = np.array(target)
        print(cs27)
        return cs27


    def convert(self):
        pass


    

if __name__ == '__main__':
    data = Data()
    data.load('viera')


