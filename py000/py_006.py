#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: python_006.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 08:47:25
############################################################################### 


def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a


i = int(input("please input: "))

print(fib(i))

