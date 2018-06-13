#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  003_02_ode.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-13 10:22:44
#  Last Modified:  2018-06-13 10:30:22
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import matplotlib.pyplot as plt
from numpy import *
from scipy.integrate import quad, dblquad, tplquad
from scipy.integrate import odeint, ode
from scipy.special import jn, yn, jn_zeros, yn_zeros


def dy(y, t, zeta, w0):
    x, p = y[0], y[1]
    dx = p
    dp = -2 * zeta * w0 * p - w0**2 * x
    return [dx, dp]


y0 = [1.0, 0.0]
t = linspace(0, 10, 1000)
w0 = 2 * pi * 1.0

y1 = odeint(dy, y0, t, args=(0.0, w0))
y2 = odeint(dy, y0, t, args=(0.2, w0))
y3 = odeint(dy, y0, t, args=(1.0, w0))
y4 = odeint(dy, y0, t, args=(5.0, w0))

fig, ax = plt.subplots()
ax.plot(t, y1[:, 0], 'k', label="undamped", linewidth=0.25)
ax.plot(t, y2[:, 0], 'r', label="under damped")
ax.plot(t, y3[:, 0], 'g', label=r"critical damping")
ax.plot(t, y4[:, 0], 'b', label="over undamped")
ax.legend()
plt.show()
