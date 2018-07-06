#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  003.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-06 09:09:37
#  Last Modified:  2018-07-06 13:48:48
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def test(s):
    res = 0
    if s is None or len(s) == 0:
        return res
    pointer = 0
    d = {}
    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= pointer:
            pointer = d[s[i]] + 1
        temp = i - pointer + 1
        d[s[i]] = i
        res = max(res, temp)
    return res


# print(test("abba"))
print(test("abbscac"))
# print(test("pwwkew"))
