#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  pysocket_server.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-28 10:47:13
#  Last Modified:  2018-05-30 16:30:22
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import socket
import commands

HOST = '127.0.0.1'
PORTRT = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTRT))
s.listen(1)

while True:
    (conn, addr) = s.accept()
    print('connected by', addr)
    while True:
        data = conn.recv(1024)
        (cmd_status, cmd_result) = commands.getstatusoutput(data)
        if len(cmd_result.strip()) == 0:
            conn.sendall('Done')
        else:
            conn.sendall(cmd_result)
conn.close()
