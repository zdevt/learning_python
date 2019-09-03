#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       FileName:  rds.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-28 09:57:03
#  Last Modified:  2019-09-03 23:15:15
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('apple', 'cccccab')

print(r.get('apple'))
