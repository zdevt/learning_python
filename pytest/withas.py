#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  withas.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-01 15:11:19
#  Last Modified:  2018-06-01 15:13:47
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        print("i am doing something")


with Sample() as sa:
    sa.do_something()
