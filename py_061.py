#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_061.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-30 20:47:25
############################################################################### 


def GetL( l ):
    if len(l) < 2 :
        l.append(1)
        return l
    else:
        l = [
                l[i]+l[i+1]
                for i in range(len(l)-1)
            ]
        l.insert(0,1)
        l.append(1)
        return l

def GetN ( n):
    l = []
    for i in range(n):
        l = GetL(l)
    return l

L = [ GetN(n) for n in range(0,11)]

for Ll in L:
    print("{}".format(Ll))

