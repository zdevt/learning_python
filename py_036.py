#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: py_036.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-30 09:40:52
############################################################################### 


def GetN(m,n):
    for i in range(m,n+1):
        for j in range(2,i):
            if i % j == 0 :
                break
        else: #for循环的else 分支,在正常结束会执行，如果是break结束则不执行else
            print(i)

GetN(3,10)


for i in range(1,5):
    print(i,i)
else:
    print("asdf",i)

