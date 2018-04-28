#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: python_001.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-16 09:19:13
############################################################################### 

'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ( i != k ) and ( i != j ) and ( j != k):
                print i,j,k

'''
'''
from itertools import permutations as pm

for i in pm([1,2,3,4],3):
    print (i)
'''

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ( i != k ) and ( i !=j) and ( j != k ):
                print(i,j,k)
