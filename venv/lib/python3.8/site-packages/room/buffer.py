#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
import time
from zmq.eventloop.ioloop import PeriodicCallback
from abc import ABCMeta,abstractmethod

from room import zmq_base as base
from room.publisher import Publisher

class BufferModule(base.ZmqProcess):

    def __init__(self, recv_addr, send_addr, recv_title, send_title, state_handler, period=1000):
        super().__init__()
        self.sub_stream    = None
        self.timer         = None        
        self.recv_addr     = recv_addr
        self.recv_title    = recv_title
        self.state_handler = state_handler
        self.period        = period
        self.callback      = Callback(Publisher(send_addr, send_title), self.state_handler)
        
    def setup(self):
        super().setup() 
        self.sub_stream, _ = self.stream(zmq.SUB, self.recv_addr, bind=False, subscribe=self.recv_title.encode('utf-8'))
        self.sub_stream.on_recv(SubStreamHandler(self.sub_stream, self.stop, self.state_handler))
        self.timer = PeriodicCallback(self.callback, self.period, self.loop)

    def run(self):
        self.setup()
        print('Start loop!')
        self.timer.start()        
        self.loop.start()

    def stop(self):
        self.loop.stop()

        
class SubStreamHandler(base.MessageHandler):
    
    def __init__(self, sub_stream, stop, state_handler):
        super().__init__()
        self._sub_stream = sub_stream
        self._stop = stop
        self._state_handler = state_handler

    def execute(self, data):
        self._state_handler.buffering(data)
        
    def stop(self, data):
        self._stop()


class StateHandler(metaclass=ABCMeta):

    @abstractmethod
    def dump(self):
        raise NotImplementedError()

    @abstractmethod    
    def buffering(self, data):
        raise NotImplementedError()        

    
class Callback(object):

    def __init__(self, publisher, state_handler):
        self.publisher = publisher
        self.state_handler = state_handler

    def __call__(self):
        data = self.state_handler.dump()
        self.publisher.send(data)
    
