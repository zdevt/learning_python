#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_018.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 13:21:43
############################################################################### 


num = int(input("please input num: "))
cnt = int(input("please input cnt: "))

def arr(n,c):
    r = 0
    for i in range(c):
        r += n*10**i
    return r

l = list(map( lambda i : arr(num,i), range(1,cnt+1)))

print(sum(l))




