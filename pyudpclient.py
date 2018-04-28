#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: pyudpclient.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-29 13:38:11
############################################################################### 

import socket


address = ('127.0.0.1',31500)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = raw_input()
    if not msg:
        break
    s.sendto(msg,address)

s.close()

