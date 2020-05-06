#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import zmq
import json
from zmq.eventloop.ioloop import PeriodicCallback
from abc import ABCMeta, abstractmethod

from room import zmq_base as base
from room.publisher import Publisher

class ParserModule(base.ZmqProcess):

    def __init__(self, recv_addr, send_addr, recv_title, send_title, category, parser):
        '''
        @param category: {'sensor', 'appliance'}

        '''
        super().__init__()
        self.sub_stream = None        
        self.recv_addr = recv_addr
        self.send_addr = send_addr
        self.recv_title = recv_title
        self.send_title = send_title
        self.category = category
        self.parser = parser

    def setup(self):
        super().setup()
        self.sub_stream, _ = self.stream(zmq.SUB, self.recv_addr, bind=False, subscribe=self.recv_title.encode('utf-8'))
        self.sub_stream.on_recv(SubStreamHandler(self.sub_stream, self.stop, self.send_addr, self.send_title, self.category, self.parser))

    def run(self):
        self.setup()
        print('Start loop!')
        self.loop.start()

    def stop(self):
        self.loop.stop()

class SubStreamHandler(base.MessageHandler):
    
    def __init__(self, sub_stream, stop, send_addr, send_title, category, parser):
        super().__init__()
        self._sub_stream = sub_stream
        self._stop = stop
        self._parser = parser
        self._send_title = send_title
        self._category = category
        self._publisher = Publisher(send_addr)

    def execute(self, data):
        parsed_data = self._parser.parse(data)
        if parsed_data:
            self._publisher.send({'category': self._category, 'msg':parsed_data}, self._send_title)
        
    def stop(self, data):
        self._stop()


class Parser(metaclass=ABCMeta):

    @abstractmethod
    def parse(self, data):
        '''
        @return [tuple(category, state)]

        state must {"key": "value"}
        '''
        raise NotImplementedError()

