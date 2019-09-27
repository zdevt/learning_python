#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  sci_o.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-04 16:48:28
#  Last Modified:  2019-09-03 17:41:21
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import scipy.optimize as opt
import scipy.integrate as inte


def f2(p):
    x, y = p
    return [(x - 5)**2 + (y - 5)**2 - 5**2, x**2 + (y - 10)**2 - 10**2]


r1 = opt.fsolve(f2, [0, 0])
r2 = opt.fsolve(f2, [10, 10])

x1 = r1[0]
x2 = r2[0]

print(x1)
print(x2)


def ff1(x):
    return 2 * (5**2 - (x - 5)**2)**0.5


s1 = inte.quad(ff1, 0, x1)
print(s1)


def ff2(x):
    return (5**2 - (x - 5)**2)**0.5 + 5 + (10**2 - x**2)**0.5 - 10


s2 = inte.quad(ff2, x1, x2)
print(s2)
