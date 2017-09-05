#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 18:55
# @Author  : heliang
import sys
import re
sum = 0
for line in open("openssh.txt"):
    reg = r'192.168'
    pipei = re.compile(reg)
    result = re.findall(reg,line)
    if result:
        sum = sum +1
        newlines = line.split()[4]
        reg2 =r'\d'
        pipei2 = re.compile(reg2)
        result2 = re.findall(reg, newlines)
        print newlines
        # if result2:
        #     print newlines
            # pass

        # if result2
            # print newlines
            # pass
        # print result

# print sum



