#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  sq_wave.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-03 10:36:31
#  Last Modified:  2019-09-03 12:19:00
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(100))
k = 2 * k - 1
f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i]) / k)
f = (4 / np.pi) * f

plt.plot(t, f)
plt.show()
