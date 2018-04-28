#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_017.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 13:17:59
############################################################################### 


import string

s = input("please input a string")


letters = 0
space = 0
digit = 0
other = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other +=1

print("c=%d s=%d d=%d o=%d" %(letters,space,digit,other))

