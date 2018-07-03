#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  funarg.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-07 10:44:53
#  Last Modified:  2018-06-07 10:46:34
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import sys


def cor(name, *a):
    print(name, a)


if __name__ == "__main__":
    cor('test', (3, 4))
