#!usr/bin/python2

import socket
import commands

#               type of ip v4 , type of protocol UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("hello python",("192.168.10.20",8000))

