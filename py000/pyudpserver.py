#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: pyudpserver.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-29 13:34:32
############################################################################### 

import socket


address = ('127.0.0.1',31500)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(address)

while True:
    data,addr = s.recvfrom(2048)
    if not data:
        print 'client has exist'
        break
    print 'received:', data, "from",addr

s.close()


