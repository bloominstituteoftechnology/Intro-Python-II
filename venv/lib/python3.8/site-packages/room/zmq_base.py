#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
import multiprocessing
from zmq.eventloop import ioloop, zmqstream
from zmq.utils import jsonapi as json

class ZmqProcess(multiprocessing.Process):
    """
    This is the base for all processes and offers utility functions 
    for setup and creating new streams.

    """
    def __init__(self):
        super().__init__()

        self.context = None
        """The ØMQ :class:`~zmq.Context` instance."""

        self.loop = None
        """PyZMQ's event loop (:class:`~zmq.eventloop.ioloop.IOLoop`)."""
        
    def setup(self):
        """
        Creates a :attr:`context` and an event :attr:`loop` for the process.

        """
        self.context = zmq.Context()
        self.loop = ioloop.IOLoop.instance()
        

    def stream(self, sock_type, addr, bind, callback=None, subscribe=b''):
        """
        Creates a :class:`~zmq.eventloop.zmqstream.ZMQStream`.

        :param sock_type: The ØMQ socket type (e.g. ``zmq.REQ``)
        :param addr: Address to bind or connect to formatted as *host:port*,
                *(host, port)* or *host* (bind to random port).
                If *bind* is ``True``, *host* may be:

                - the wild-card ``*``, meaning all available interfaces,
                - the primary IPv4 address assigned to the interface, in its
                numeric representation or
                - the interface name as defined by the operating system.

                If *bind* is ``False``, *host* may be:

                - the DNS name of the peer or
                - the IPv4 address of the peer, in its numeric representation.

                If *addr* is just a host name without a port and *bind* is
                ``True``, the socket will be bound to a random port.
        :param bind: Binds to *addr* if ``True`` or tries to connect to it
                otherwise.
        :param callback: A callback for
                :meth:`~zmq.eventloop.zmqstream.ZMQStream.on_recv`, optional
        :param subscribe: Subscription pattern for *SUB* sockets, optional,
                defaults to ``b''``.
        :returns: A tuple containg the stream and the port number.

        """
        sock = self.context.socket(sock_type)

        # addr may be `host:port` or ('host', port)
        if isinstance(addr, str):
            addr = addr.split(':')
            host, port = addr if len(addr) == 2 else (addr[0], None)

        # Bind/connect the socket
        if bind:
            if port:
                sock.bind('tcp://%s:%s' % (host, port))
            else:
                port = sock.bind_to_random_port('tcp://%s' % host)
        else:
            sock.connect('tcp://%s:%s' % (host, port))
                
        # Add a default subscription for SUB sockets
        if sock_type == zmq.SUB:
            sock.setsockopt(zmq.SUBSCRIBE, subscribe)
             
        # Create the stream and add the callback
        stream = zmqstream.ZMQStream(sock, self.loop)
        if callback:
            stream.on_recv(callback)

        return stream, int(port)
    

class  MessageHandler(object):
    """
    Base class for message handlers for a :class:`ZMQProcess`.
    
    Inheriting classes only need to implement a handler function for each message type.

    """

    def __call__(self, msg):
        """
        Gets called when a messages is recieved by the stream this handlers is
        registered at. *msg* is a list as return by
        :meth:`zmq.core.socket.Socket.recv_multipart`.
        """

        method = msg[1].decode('utf-8')
        data = json.loads(msg[2])
        # Get the actual message handler and call it
        if method.startswith('_'):
            raise AttributeError('%s starts with an "_"' % method)

        getattr(self, method)(data)

