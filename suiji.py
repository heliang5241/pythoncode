#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 11:14
# @Author  : heliang
from random import choice
import string
#python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
def GenPassword(length=8,chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

if __name__=="__main__":
    for i in range(10):
        print(GenPassword(8))
