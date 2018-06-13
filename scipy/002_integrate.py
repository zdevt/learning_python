#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  002_integrate.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-13 09:26:33
#  Last Modified:  2018-06-13 10:22:12
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

from numpy import *
from scipy.integrate import quad, dblquad, tplquad
from scipy.special import jn, yn, jn_zeros, yn_zeros


def f(x):
    return x


x_lower = 0
x_upper = 1

val, abserr = quad(f, x_lower, x_upper)

print("integral value=", val, ",absolute error=", abserr)


def integrand(x, n):
    return jn(n, x)


x_lower = 0
x_upper = 10

val, abserr = quad(integrand, x_lower, x_upper, args=(3, ))
print("integral value=", val, ",absolute error=", abserr)

val, abserr = quad(lambda x: exp(-x**2), -Inf, Inf)
print("integral value=", val, ",absolute error=", abserr)

analytical = sqrt(pi)
print("analytical=", analytical)


def integrand(x, y):
    return exp(-x**2 - y**2)


x_lower = 0
x_upper = 10
y_lower = 0
y_upper = 10

val, abserr = dblquad(integrand, x_lower, x_upper, lambda x: y_lower,
                      lambda x: y_upper)
print("integral value=", val, ",absolute error=", abserr)
