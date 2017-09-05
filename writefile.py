#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/4 12:46
# @Author  : heliang
f = file('0804.txt','a+')
li = ["hello world\n","hello passwd\n"]
f.writelines(li)
# f.write(kli)
f.close()
