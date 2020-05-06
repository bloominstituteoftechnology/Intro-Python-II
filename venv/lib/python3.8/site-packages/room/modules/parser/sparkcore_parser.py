#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from room import parser
from room.utils.config import network_config

class SparkCoreParserModule(parser.ParserModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder1']['back']),
            send_addr=int(network_config['forwarder2']['front']),            
            recv_title='sparkcore',
            send_title='',
            category='sensor',
            parser=SparkCoreParser()
        )

class SparkCoreParser(parser.Parser):
        
    def parse(self, data):
        data.pop('time')
        coreId = data.pop('sensorId')
        return [{coreId + "_" + key: data[key]} for key in data.keys()]

if __name__ == "__main__":
    process = SparkCoreParserModule()
    process.run()
        
