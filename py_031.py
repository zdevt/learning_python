#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_031.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-30 08:10:00
############################################################################### 

l = ['Monday', 'Tuesday','Thursday','Wednesday','Friday','Saturday','Sunday']
s = input("Please input s:")

def SearchS(l,s):
    slen = len(s)
    for ll in l:
        if ll[0:slen] == s:
            return ll
    return "None"

print( SearchS(l,s))
