#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  650.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-17 14:19:30
#  Last Modified:  2018-07-18 08:50:57
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

    (x,y)=(1,n)
    for i in range(2, n // 2):
        v = n / i
        if v.is_integer():
            (x,y)=(i,int(v))
            break

    if x == 1:
        return y

    return MinSteps(x) + MinSteps(y)

print(MinSteps(188))
