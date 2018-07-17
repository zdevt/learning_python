#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  650.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-17 14:19:30
#  Last Modified:  2018-07-17 16:45:01
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def MinSteps(n):
    if n == 1:
        return 0

    if n == 2:
        return 2

    if n == 3:
        return 3

    l = []
    for i in range(2, n):
        v = n / i
        if v.is_integer():
            l.append((i, int(v)))

    l.sort(key=lambda e: e[0] + e[1])
    (x, y) = l[0]
    return MinSteps(min(x, y)) + max(x, y)


print(MinSteps(9))
