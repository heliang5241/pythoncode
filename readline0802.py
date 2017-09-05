#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 20:34
# @Author  : heliang
import os
def VisitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print pathname
def shanchu():
    if os.path.exists('test2.txt'):
        os.remove('test2.txt')
if __name__ == '__main__':
    # path = r"D:\BaiduNetdiskDownload"
    # VisitDir(path)
    shanchu()

