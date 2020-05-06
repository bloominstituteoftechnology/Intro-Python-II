#!/usr/bin/env python3
# -*- coding: utf-8- 

import zmq
import time

class Subscriber():

    def __init__(self, bind_addr, subscriber=b''):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect('tcp://' + bind_addr)
        self.socket.setsockopt(zmq.SUBSCRIBE, subscriber)
        time.sleep(1.0)
        
    def recv(self):
        return self.socket.recv_multipart()

    def stop(self):
        self.socket.close()
        self.context.term()
     

