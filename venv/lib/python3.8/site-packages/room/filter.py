#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
from abc import ABCMeta, abstractmethod

from room import zmq_base as base
from room.publisher import Publisher

class FilterModule(base.ZmqProcess):

    def __init__(self, recv_addr, send_addr, recv_title, send_title, filter):

        super().__init__()
        self.sub_stream = None        
        self.recv_addr  = recv_addr
        self.send_addr  = send_addr
        self.recv_title = recv_title
        self.send_title = send_title
        self.filter     = filter

    def setup(self):
        super().setup()
        self.sub_stream, _ = self.stream(zmq.SUB, self.recv_addr, bind=False, subscribe=self.recv_title.encode('utf-8'))
        self.sub_stream.on_recv(SubStreamHandler(self.sub_stream, self.stop, self.send_addr, self.send_title, self.filter))

    def run(self):
        self.setup()
        print('Start loop!')
        self.loop.start()

    def stop(self):
        self.loop.stop()


class SubStreamHandler(base.MessageHandler):
    
    def __init__(self, sub_stream, stop, send_addr, send_title, filter):
        super().__init__()
        self._sub_stream = sub_stream
        self._stop = stop
        self._send_title = send_title
        self._filter = filter
        self._publisher = Publisher(send_addr)

    def execute(self, data):
        result = self._filter.filtrate(data)
        if result:
            self._publisher.send(result, self._send_title)
                
    def stop(self, data):
        self._stop()

        
class Filter(metaclass=ABCMeta):

    @abstractmethod
    def filtrate(self, data):
        raise NotImplementedError()            
    
