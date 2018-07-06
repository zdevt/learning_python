#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  537.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-06 16:47:59
#  Last Modified:  2018-07-06 16:58:47
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def Test(x, y):
    R = 0
    I = 0
    a, b, c, d = 0, 0, 0, 0
    sx = x.split('+')
    sy = y.split('+')
    a = int(sx[0])
    b = int(sx[1].strip('i'))
    c = int(sy[0])
    d = int(sy[1].strip('i'))

    R = a * c - b * d
    I = a * d + b * c

    S = str(R) + "+" + str(I) + "i"

    return S


print(Test("1+1i", "1+-1i"))
