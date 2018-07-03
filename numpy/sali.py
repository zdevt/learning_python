#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  sali.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-03 10:37:11
#  Last Modified:  2018-07-03 10:37:16
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys
# (1) 使用linspace函数初始化变量t，即从-pi到pi上均匀分布的201个点
a = float(9)
b = float(8)
t = np.linspace(-np.pi, np.pi, 201)
# (2) 使用sin函数和NumPy常量pi计算变量x
x = np.sin(a * t + np.pi / 2)
# (3) 使用sin函数计算变量y
y = np.sin(b * t)
plot(x, y)
show()
