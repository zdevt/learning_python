#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  3door3.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-03 15:47:44
#  Last Modified:  2018-07-04 11:31:42
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import numpy.random as rd

w_doors = rd.randint(0, 3, 1000)

i_cnts = 0
c_cnts = 0


for w_door in w_doors:
    f_try = rd.randint(0, 3)
    remain_c = [i for i in range(0, 3) if i != f_try]
    wrong_c = [i for i in range(0, 3) if i != w_door]

    if f_try in wrong_c:
        wrong_c.remove(f_try)

    remain_c.remove(rd.choice(wrong_c))

    if f_try == w_door:
        i_cnts += 1

    if remain_c[0] == w_door:
        c_cnts += 1

print("i=", i_cnts, "c=", c_cnts)
