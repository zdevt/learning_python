#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  542.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-09 16:57:12
#  Last Modified:  2018-07-10 10:08:55
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

for k in range(1, 4):
    l = [(x, y) for x in range(-k, k + 1, 1) for y in range(-k, k + 1, 1)
         if (abs(x) + abs(y)) == k]

    print(l)
