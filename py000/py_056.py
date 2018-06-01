#!/usr/bin/env python
#-*- coding:utf-8 -*-
###############################################################################
#       File Name: py_056.py
#          Author:
#            Mail:
#    Created Time: 2017-10-30 16:09:24
###############################################################################

from tkinter import *

canvas = Canvas(width=800, height=600, bg='yellow')
canvas.pack(expand=YES, fill=BOTH)

k = 1
j = 1

for i in range(0, 26):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
    k += j
    j += 0.3

mainloop()
