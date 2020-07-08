# -*- coding: utf-8 -*-

from pymongo import MongoClient
from room.utils.config import config

class Data(object):

    def __init__(self):
        self._client     = MongoClient(config['mongo']['host'], int(config['mongo']['port']))
        self._db         = self._client[config['mongo']['db']]
        self._collection = self._db[config['mongo']['collection']]
        

    def load(self):
        previous_state = {}
        result = []
        
        for record in self._collection.find():
            inout = record['inout']
            appliances = record['appliances']
            state = {}
            state.update(inout)
            state.update(appliances)

            for key, value in state.items():
                if not key in previous_state or previous_state[key] != value:
                    previous_state[key] = value
                    result.append((key,value))
                    
        return result
            
    def save(self):
        pass


if __name__ == '__main__':
    data = Data()
    print(data.load())
