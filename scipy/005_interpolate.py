#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  005_interpolate.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-13 11:05:00
#  Last Modified:  2019-09-03 10:50:53
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import matplotlib.pyplot as plt

import numpy as np

import scipy.interpolate as scin


def f(x):
    return np.sin(x)


n = np.arange(0, 10)
x = np.linspace(0, 9, 100)
y_meas = f(n) + 0.1 * np.random.randn(len(n))
y_real = f(x)

linear_interpolation = scin.interp1d(n, y_meas)
y_interp1 = linear_interpolation(x)

cublic_interpolation = scin.interp1d(n, y_meas, kind='cubic')
y_interp2 = cublic_interpolation(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(n, y_meas, 'bs', label='noisy_data')
ax.plot(x, y_real, 'k', lw=2, label='true function')
ax.plot(x, y_interp1, 'r', label='linear interp')
ax.plot(x, y_interp2, 'g', label='cubic interp')
ax.legend(loc=3)
plt.show()
