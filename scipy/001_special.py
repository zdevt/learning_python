#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  001_special.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-13 09:13:12
#  Last Modified:  2018-06-26 15:11:12
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import matplotlib.pyplot as plt

from numpy import *
from scipy.special import jn, yn, jn_zeros, yn_zeros

n = 0
x = 0.0

print("J_%d(%f)=%f" % (n, x, jn(n, x)))

x = 1.0
print("Y_%d(%f)=%f" % (n, x, yn(n, x)))

x = linspace(0, 10, 100)

fig, ax = plt.subplots()

for n in range(4):
    ax.plot(x, jn(n, x), label=r"$J_%d(x)$" % n)
ax.legend()

plt.show()

n = 0
m = 4
jn_zeros(n, m)
