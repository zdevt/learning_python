#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_069.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-31 10:37:40
############################################################################### 

n = int(input(":"))


l = [ i for i in range(1,n+1)]


sum = 0
while True:
    t = 0
    for i in range(1,len(l)+1):
        sum += 1
        if sum %3 == 0:
            l.pop(i-1-t)
            t += 1

    if len(l) == 1:
        break

print(l)
