#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: guangtou.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-31 22:28:00
############################################################################### 

from sympy import Circle
from scipy import integrate
from math import sqrt

c1=Circle((1,0),1)
c2=Circle((1/2,1),1/2)
jiaodian = c1.intersection(c2)
print(jiaodian)
#求出交点:[Point2D(1/5, 3/5), Point2D(1, 1)]

def func(x):
    return sqrt(2*x-x**2)-1+sqrt(x-x**2)

p,err = integrate.quad(func,0.2,1.0)
print(p)

