#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  plot.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-06 15:43:52
#  Last Modified:  2018-06-26 16:01:47
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)

plt.xlim((-12, 12))
plt.ylim((-12, 12))

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

theta = np.arange(0, 2 * np.pi, 2 * np.pi / 100)
x = np.cos(theta)
y = np.sin(theta)
ax.plot(x, y)

plt.show()
