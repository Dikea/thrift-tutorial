#!/bin/env python
#-*- encoding: utf-8 -*-


import sys
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from Hello import HelloService



def enable_client():
    try:
        transport = TSocket.TSocket('localhost', 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = HelloService.Client(protocol)
        transport.open()

        print "client - say"
        msg = client.say("Hello!")
        print "server - " + msg

        transport.close()
    except Thrift.TException, ex:
        print "errmsg=%s" % (ex.message)


if __name__ == '__main__':
    enable_client()
