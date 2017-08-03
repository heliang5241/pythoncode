#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 10:26
# @Author  : heliang
"""
1、读取该文件，并输出所有内容
2、去掉文件内容中的换行
3、计算出文件的长度
4、使用欧冠代替2014
5、创建另一个文件test2.txt,写入本文件的内容
"""
def getTxt():
    f = open('tmp.txt','w')
    txt = """今年是2014年
2014年你好
2014年再见
    """
    f.write(txt)
    f.close()
def chuli():
    f = open('tmp.txt','r+')
    print f.read()
if __name__ == '__main__':
    # getTxt()
    chuli()


