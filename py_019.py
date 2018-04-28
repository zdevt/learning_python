#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_019.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 14:13:18
############################################################################### 


def GetList( num ):
    res = []
    for i in range(1,num):
        if num % i == 0:
            res.append(i)
    return res

for i in range(1,1001):
    if i == sum(GetList(i)):
        print(i)

