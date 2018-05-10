#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_022.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-28 16:29:14
############################################################################### 



for i in ['a','b','c']:
    for j in ['x','y','z']:
        if not(i =='a' and j == 'x') and \
           not(i =='c' and (j == 'x' or j == 'z') ):
            print(i,j)

