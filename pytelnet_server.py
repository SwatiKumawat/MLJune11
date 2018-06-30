#!/usr/bin/python2 

import socket 
import commands
#               type of ip v4   type of protocol UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind current ip and port

s.bind(("192.168.10.20",8000))

# buffer size i.e data received per client at single send
for i in range (1000) :

	data=s.recvfrom(100)
	if 'date' in data[0]:
		print data[0]
		print commands.getoutput('date')
	elif 'cal' in data[0]:
		print data[0]
		print commands.getoutput('cal')
	else:
		print data
		print commands.getoutput(data[0])

