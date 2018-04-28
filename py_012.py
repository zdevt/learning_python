#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_012.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 09:55:02
############################################################################### 


from math import sqrt


def Issu( a ):
    k = int(sqrt(a))
    for i in range(2,k+1):
        if a % i == 0:
            return False
    return True

for l in range(101,201):
    if ( Issu( l )):
        print( l )




