#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: python_003.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-16 09:51:07
############################################################################### 

x1 = map ( lambda i : i*i - 100,range(1,100))
x2 = map ( lambda i : i*i - 100-168,range(1,100))

l1 = list(x1)
l2 = list(x2)


print( set(l1) & set(l2))

