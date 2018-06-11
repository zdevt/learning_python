#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       FileName:  rds.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-28 09:57:03
#  Last Modified:  2018-06-11 14:09:36
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import redis

r = redis.Redis('192.168.18.88', 16379)
r.set('apple', 'ab')

print r.get('apple')

