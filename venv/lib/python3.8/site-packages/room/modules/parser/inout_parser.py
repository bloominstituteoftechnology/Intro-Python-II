#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from room import parser
from room.utils.config import network_config

class InOutParserModule(parser.ParserModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder1']['back']),
            send_addr=int(network_config['forwarder2']['front']),            
            recv_title='inout',
            send_title='event',
            category='inout',
            parser=InOutParser()
        )

class InOutParser(parser.Parser):
        
    def parse(self, data):
        return [{user: 1 if data[user] == 'in' else 0 } for user in data.keys()]

    
if __name__ == "__main__":
    process = InOutParserModule()
    process.run()


