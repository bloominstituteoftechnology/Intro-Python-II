#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from room import parser
from room.utils.config import network_config

class DefaultParserModule(parser.ParserModule):

    def __init__(self):
        super().__init__(
            recv_addr='localhost:{0}'.format(network_config['forwarder1']['back']),
            send_addr=int(network_config['forwarder2']['front']),                        
            recv_title='default',
            send_title='',
            parser=DefaultParser()
        )

class DefaultParser(parser.Parser):

    def parse(self, data):
        return data

    
if __name__ == "__main__":
    process = DefaultParserModule()
    process.run()

