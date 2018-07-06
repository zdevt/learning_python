#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  003.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-06 09:09:37
#  Last Modified:  2018-07-06 09:32:25
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def test(s):
    res = 0
    if s is None or len(s) == 0:
        return res
    d = {}
    tmp = 0
    start = 0
    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
            start = d[s[i]] + 1
        tmp = i - start + 1
        d[s[i]] = i
        res = max(res, tmp)
    return res


print(test("abba"))
print(test("abbscac"))
print(test("pwwkew"))
