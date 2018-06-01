#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  tkinter.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-01 16:38:23
#  Last Modified:  2018-06-01 16:41:23
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

from Tkinter import *
root = Tk()

li = ['c', 'python', 'php']
movie = ['css', 'jquery', 'bootstrap']
listb = Listbox(root)
listb2 = Listbox(root)

for item in li:
    listb.insert(0, item)

for item in movie:
    listb2.insert(0, item)

listb.pack()
listb2.pack()
root.mainloop()
