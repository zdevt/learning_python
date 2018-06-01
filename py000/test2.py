#!/usr/bin/python
#-*- coding:utf-8 -*-
###############################################################################
#       File Name: test.py
#          Author:
#            Mail:
#    Created Time: 2017-10-07 15:48:09
###############################################################################


def Add(a, b):
    print 'a+b', a + b


class TestClass:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print self.name
