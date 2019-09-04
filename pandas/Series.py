#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  data.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2019-09-04 13:04:12
#  Last Modified:  2019-09-04 14:20:34
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import pandas as pd


df1 = pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
df2 = pd.DataFrame.from_dict(dict([('A', [3, 2, 3]), ('B', [4, 5, 6])]))

# print(df1)
# print(df2)

x = pd.Series([df1], index=['aaa'])
y = pd.Series([df2], index=['bbb'])
x = x.append(y)
print(x)
