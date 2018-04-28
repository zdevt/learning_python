#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_011.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 09:09:33
############################################################################### 

f1 = 1
f2 = 1

i = int(input("plase input: "))

j = i // 3

for a in range(j):
    f1,f2= f2,f1+f2

print(f2)
