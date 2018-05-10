#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_014.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 11:32:23
############################################################################### 

i = int(input("please input: "))


temp = []

while i != 1:
    for j in range(2,i+1):
        if i % j == 0:
            temp.append(j)
            i = i//j
            break

print(temp)

