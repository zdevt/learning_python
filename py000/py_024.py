#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_024.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 22:25:49
############################################################################### 

# 2/1,3/2,5/3,8/5 ......


def GetN(n):
    a = 2.0
    b = 1.0
    c = 0
    for i in range(n):
        a,b = (a+b),a
    return a/b


l = list(map(lambda x : GetN(x), range(20)))

#print(l)
print(sum(l))
