#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 10:52
# @Author  : heliang
from random import choice
import string

def GenPassword(length=8,chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

def getiplist():
    f = open('iplist.txt','w+')
    for i in range(1,3):
        iplist = '192.168.1.' + str(i) + ' ' + GenPassword(5)
        f.write(iplist)
        f.write('\n')
    f.close()

if __name__ == '__main__':
    # getiplist()


