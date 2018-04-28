#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_020.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 15:26:51
############################################################################### 

def GetRes( h, cnt):
    l = list(map(lambda cnt : h*(1/2)**(cnt),range(1,cnt+1)))
    print(l)
    return sum(l)*2+100,l[cnt-1]

print(GetRes(100,10))


