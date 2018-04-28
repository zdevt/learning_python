#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_041.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-30 15:35:57
############################################################################### 

def varfunc():
    var = 0
    print("var=%d" %var)
    var +=1

if __name__ == '__main__':
    for i in range(3):
        varfunc()



class Static:
    staticvar = 5
    def varfunc(self):
        self.staticvar += 1
        print(self.staticvar)

a=Static()

for i in range(3):
    a.varfunc()

