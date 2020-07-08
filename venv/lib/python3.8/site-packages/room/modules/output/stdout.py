#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from room.output import OutputModule, Action
from room.utils.config import network_config

class StdOutModule(OutputModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder5']['back']),            
            recv_title='',
            action=StdOut()
        )

class StdOut(Action):

    def action(self, data):
        print(data)

if __name__ == '__main__':
    process = StdOutModule()
    process.run()
