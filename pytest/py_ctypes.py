#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  ccc.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-26 15:43:20
#  Last Modified:  2018-06-26 15:46:05
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

from ctypes import *
from platform import *

cdll_names = {
    'Darwin': 'libc.dylib',
    'Linux': 'libc.so.6',
    'Windows': 'msvcrt.dll'
}

clib = cdll.LoadLibrary(cdll_names[system()])
clib.printf(c_char_p("Hello %d %f\n"), c_int(15), c_double(2.3))

