#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_009.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 09:02:05
############################################################################### 

import time

myD = { 1: 'a', 2:'b'}

for k,v in dict.items(myD):
    print(k,v)
    time.sleep(1)

