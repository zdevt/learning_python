#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  t.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-05 16:08:52
#  Last Modified:  2019-09-03 22:49:31
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

from itertools import cycle

playerIndexGen = cycle([0, 1, 2, 1])

print(next(playerIndexGen))
print(next(playerIndexGen))
print(next(playerIndexGen))
print(next(playerIndexGen))

print(next(playerIndexGen))
print(next(playerIndexGen))
print(next(playerIndexGen))
print(next(playerIndexGen))
