#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  001_special.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-13 09:13:12
#  Last Modified:  2019-09-03 10:40:43
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import matplotlib.pyplot as plt

import numpy as np
from scipy.special import jn, yn, jn_zeros

n = 0
x = 0.0

print("J_%d(%f)=%f" % (n, x, jn(n, x)))

x = 1.0
print("Y_%d(%f)=%f" % (n, x, yn(n, x)))

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()

for n in range(4):
    ax.plot(x, jn(n, x), label=r"$J_%d(x)$" % n)
ax.legend()

plt.show()

n = 0
m = 4
jn_zeros(n, m)
