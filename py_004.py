#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: python_004.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 08:42:26
############################################################################### 

import time

D =input("please input xxxx-xx-xx:")
d = time.strptime(D,'%Y-%m-%d').tm_yday

print("the {} day ".format(d))


