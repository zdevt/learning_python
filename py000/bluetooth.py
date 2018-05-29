#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  bt.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-29 10:14:31
#  Last Modified:  2018-05-29 10:18:10
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import time
import bluetooth
alreadyFound = []


def findDevs():
    foundDevs = bluetooth.discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in alreadyFound:
            print '[*] Found Bluetooth Device : ' + str(name)
            print '[+] Mac address : ' + str(addr)
            alreadyFound.append(addr)


while True:
    findDevs()
    time.sleep(3)
