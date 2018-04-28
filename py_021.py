#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_021.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 15:59:49
############################################################################### 

def GetM(n):
    xn = 1
    for i in range(n-1):
        xn = (xn+1)*2
    return xn

print(GetM(10))

