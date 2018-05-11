#!/bin/env python
#-*- encoding: utf-8 -*-


import sys
sys.path.append('gen-py')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from Hello import HelloService
from Hello.ttypes import *


class HelloServiceHandler(object):

    def say(self, msg):
        ret = 'received' + msg
        print ret
        return ret


def start_server():
    handler = HelloServiceHandler()
    processor = HelloService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", 9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "Starting thrift server in python..."
    server.serve()
    print "done!"


if __name__ == '__main__':
    start_server()


