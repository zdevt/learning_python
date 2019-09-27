#!/usr/bin/env python
# -*- coding:utf-8 -*-
#       FileName:  mat_test.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-07-03 10:38:08
#  Last Modified:  2019-08-30 16:23:58
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import numpy as np

A = np.mat('1 2 3;4 5 6;7 8 9')

print(A)
print(A.T)

print(np.mat(np.arange(24)).reshape(6, 4))

A = np.eye(2)
print("A", A)

A = np.eye(3)
print(A)

B = A * 2
print(B)
print(np.bmat('A B;A B'))
