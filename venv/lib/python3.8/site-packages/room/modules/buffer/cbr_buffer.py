#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from room.buffer import BufferModule, StateHandler
from room.state import State
from room.utils.config import config
from room.utils.config import network_config

class CBRBufferModule(BufferModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder3']['back']),
            send_addr=int(network_config['forwarder7']['front']),
            recv_title='buffer',
            send_title='cbr',
            state_handler=CBRStateHandler(),
            period=int(config['cbr_buffer']['interval_ms'])
        )
        
class CBRStateHandler(StateHandler):

    def __init__(self):
        self._records = []
    
        
    def dump(self):

        sum = {}
        sum['appliances'] = {}
        sum['sensors'] = {}
        sum['inout'] = {}
        
        result = {}
        result['appliances'] = {}
        result['sensors'] = {}
        result['inout'] = {}
        
        num = len(self._records)
        mid = num // 2
        
        for record in self._records:
            for key, value in record['appliances'].items():
                if key not in sum['appliances']: sum['appliances'][key] = value
                else: sum['appliances'][key] += value
            for key, value in record['sensors'].items():
                if key not in sum['sensors']: sum['sensors'][key] = value                
                else: sum['sensors'][key] += value            
            for key, value in record['inout'].items():
                if key not in sum['inout']: sum['inout'][key] = value                                
                else: sum['inout'][key] += value            
            
        for key in sum['appliances'].keys():
            result['appliances'][key] = sum['appliances'][key] / num
        for key in sum['sensors'].keys():
            result['sensors'][key] = sum['sensors'][key] / num
        for key in sum['inout'].keys():
            result['inout'][key] = sum['inout'][key] / num            

        print(str(sum))
        result['timestamp'] = self._records[mid]['timestamp']
                
        self._records.clear()
        
        return result

    def buffering(self, data):
        self._records.append(data)

if __name__ == "__main__":
    process = CBRBufferModule()
    process.run()
    
