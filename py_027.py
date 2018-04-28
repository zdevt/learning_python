#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_027.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-29 18:31:21
############################################################################### 

s =  input("please input a string: ")

'''
print(s)
print(s[::-1])
'''

def Output(str,l):
    if l == 0 :
        return
    print(str[l-1])
    Output(str,l-1)


Output(s,len(s))


