#!/usr/bin/python
#-*- coding:utf-8 -*-
###############################################################################
#       File Name: server.py
#          Author:
#            Mail:
#    Created Time: 2017-08-22 17:11:32
###############################################################################

import socket as sk


s = sk.socket()
h = sk.gethostname()
p = 12345

s.bind((h,p))

s.listen(5)

while True:
    c,a = s.accept()
    print 'connect:', a
    c.send('welcome')
    c.close()
