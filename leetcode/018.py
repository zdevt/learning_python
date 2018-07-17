#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  018.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-07 18:06:06
#  Last Modified:  2018-07-07 18:26:50
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import itertools as it

# l = [1, 2, 3, 4]
l = "1234"

for i in it.combinations(l, 3):
    # print(i[0],i[1],i[2])
    # print(i)
    for c in i:
        print(c)
