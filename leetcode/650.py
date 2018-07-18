#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  650.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-17 14:19:30
#  Last Modified:  2018-07-18 08:33:21
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def MinSteps(n):
    if n == 1:
        return 0

    if 2 <= n <= 3:
        return n

    l = []
    for i in range(1, n // 2):
        v = n / i
        if v.is_integer():
            l.append((i, int(v)))

    l.sort(key=lambda e: e[0] + e[1])
    (x, y) = l[0]
    minv = min(x,y)
    maxv = max(x,y)
    print(l)

    if minv == 1:
        return maxv

    return MinSteps(x) + MinSteps(y)

print(MinSteps(182))
