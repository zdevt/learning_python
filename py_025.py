#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_025.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-29 18:25:57
############################################################################### 

def GetN(n):
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a


l = list(map(lambda x: GetN(x),range(1,21)))

print(sum(l))

