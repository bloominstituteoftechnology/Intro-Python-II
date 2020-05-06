#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from room.miner import MinerModule, Miner
from room.modules.miner.estimator.nnw import NeuralNetWork as NNW
from room.utils.config import network_config

class NNWModule(MinerModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder6']['back']),
            send_addr=int(network_config['forwarder5']['front']),
            recv_title='nnw',
            send_title='nnw',
            miner=NeuralNetWork(),
        )


class NeuralNetWork(Miner):

    def __init__(self):
        self.appliance = 'fan'        
        self.nnw = NNW(self.appliance)

    def mining(self, data):
        predict = self.predict(data['data'])
        return self.recommend(data['target'][self.appliance], predict)

    def predict(self, data):
        data = np.array([data]).astype(np.float32)        
        return self.nnw.predict(data)[0]

    def recommend(self, current, predict):
        if predict is not None and current != predict:            
            return [{'appliance': self.appliance, 'method': predict}]
        else:
            return []

    

if __name__ == "__main__":
    process = NNWModule()
    process.run()
    
    

