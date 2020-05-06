#!/usr/bin/env python
# -*- coding: utf-8 -*-

from room.miner import MinerModule, Miner
from room.modules.miner.estimator.speed import SPEED
from room.utils.config import network_config

class SpeedModule(MinerModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder3']['back']),
            send_addr=int(network_config['forwarder4']['front']),
            recv_title='speed',
            send_title='speed',
            miner=SpeedPack(),
        )


class SpeedPack(Miner):

    def __init__(self):
        self.speed = SPEED()

    def mining(self, data):
        result = self.speed.execute(list(data.items())[0])
        if result:
            return {result[0]:result[1]} # tuple to dict
        else:
            return []


if __name__ == "__main__":
    process = SpeedModule()
    process.run()
    
    
