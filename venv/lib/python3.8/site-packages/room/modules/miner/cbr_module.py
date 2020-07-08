#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from room.miner import MinerModule, Miner
from room.modules.miner.estimator.case_based_reasoning import CBR as cbr
from room.utils.config import network_config
from room.utils.config import config
from pymongo import MongoClient

class CBRModule(MinerModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder7']['back']),
            send_addr=int(network_config['forwarder5']['front']),                        
            recv_title='cbr',
            send_title='cbr',
            miner=CBR(),
        )

class CBR(Miner):

    def __init__(self):
        self.cbr = cbr()
        self.records = []
        self.db = MongoDB()
        self.load()

    def mining(self, data):
        result = self.cbr.recommend(data, self.records)
        self.add(data) # キューに保存
        self.pop() # 先頭削除
        return result

    def add(self, data):
        self.records.append(data)

    def pop(self):
        self.records.pop(0)
        
    def load(self):
        records = self.db.all()
        print(len(records), records[0])
        for record in records:
            self.add(record)
            
class MongoDB(object):

    def __init__(self):
        self._client     = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
        self._db         = self._client[config['mongo']['db']]
        self._collection = self._db[config['mongo']['collection']]

    def all(self):
        return [record for record in self._collection.find()]

    def restrict(self, start_index=500000): # start_indexより後のレコードを取得する
        return [record for record in self._collection.find()[start_index:]]

    
    
if __name__ == "__main__":
    process = CBRModule()
    process.run()
    
