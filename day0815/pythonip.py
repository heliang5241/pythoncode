#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 9:22
# @Author  : heliang
import re
f = open("c:/tmp0828.txt")
files = f.readline()
# print files
r =r'SUCCESS'
hehe = 0
new = re.compile(r)
compile_str = re.findall(new, files)
if compile_str:
    hehe = hehe +1
print hehe
f.close()
