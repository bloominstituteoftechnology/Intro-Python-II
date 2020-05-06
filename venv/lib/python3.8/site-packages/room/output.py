#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
from abc import ABCMeta, abstractmethod

from room import zmq_base as base

class OutputModule(base.ZmqProcess):

    def __init__(self, recv_addr, recv_title, action):
        super().__init__()
        self.sub_stream = None        
        self.recv_addr  = recv_addr
        self.recv_title = recv_title
        self.action     = action

    def setup(self):
        super().setup()
        self.sub_stream, _ = self.stream(zmq.SUB, self.recv_addr, bind=False, subscribe=self.recv_title.encode('utf-8'))
        self.sub_stream.on_recv(SubStreamHandler(self.sub_stream, self.stop, self.action))

    def run(self):
        self.setup()
        print('Start loop!')
        self.loop.start()

    def stop(self):
        self.loop.stop()
    
class SubStreamHandler(base.MessageHandler):

    def __init__(self, sub_stream, stop, action):
        super().__init__()
        self._sub_stream = sub_stream
        self._stop = stop
        self._action = action

    def execute(self, data):
        self._action.action(data)

    def stop(self, data):
        self._stop()


class Action(metaclass=ABCMeta):

    @abstractmethod
    def action(self, data):
        raise NotImplementedError()    
    
