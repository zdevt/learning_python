#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_013.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 10:06:55
############################################################################### 


def zzz(i):
    if i == (i//100)**3 + ((i%100)//10)**3 + (i%10)**3:
        return True
    return False


for i in range(100,1000):
    if zzz(i):
        print(i)

