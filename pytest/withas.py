#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  withas.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-01 15:11:19
#  Last Modified:  2018-06-29 16:00:25
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


class Sample:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, type, value, trace):
        print("exit",type,value,trace)

    def do_something(self):
        print("i am doing something")


with Sample() as sa:
    sa.do_something()
