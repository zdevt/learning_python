#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  479.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-18 09:34:57
#  Last Modified:  2018-07-19 09:00:08
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def CheckPalindrome(v):
    if v < 10:
        return True

    if v % 10 == 0:
        return False

    back = 0
    while v > back:
        back = back * 10 + v % 10
        v = v // 10

    return (v == back) or (back // 10 == v)


def largestPalindrome(n):
    n = n - 1
    temp = 0
    k = (n + 1) // 2
    for i in range((10**k - 1) * 10**(n - k + 1), 10**(n + 1)):
        for j in range((10**k - 1) * 10**(n - k + 1), 10**(n + 1)):
            if CheckPalindrome(i * j):
                temp = max(temp, i * j)
                print(i, j, i * j, temp)

    print(temp % 1337)
    return temp % 1337


def largestPalindrome2(n):
    temp = 0
    for i in range(10**(2 * n - 1), 10**(2 * n - 2),-1):
        if CheckPalindrome(i):
            temp = i
    print(temp)
    return temp % 1337


# largestPalindrome(7)
largestPalindrome2(4)
