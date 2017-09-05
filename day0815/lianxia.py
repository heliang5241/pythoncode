#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 19:58
# @Author  : heliang
#统计每个字符出现的次数，使用字典输出
import re
from collections import *
import os
str = "ab2b3n5n2n67mm4n2"
# print re.findall(r'\d',str)
# print "".join(re.findall(r'\d',str))
print len(re.findall(r'n',str))

def get_counter():
    return Counter()
def str_to_list(s):
    if s != None:
        return [x for x in s]
    else:
        return []
def counter(c, l):
    for word in l:
        c[word] += 1
    return c
def get_file_str(path):
    if os.path.exists(path):
        temp_str = ''
        with open(path, 'r') as pf:
            for line in pf:
                temp_str += line
            return temp_str
    else:
        print('the file [{}] is not exist!'.format(path))
def test_str():
    cnt = get_counter()
    temp_str = 'hello,i\'m Hongten,welcome to my space!'
    temp_list = str_to_list(temp_str)
    cnt = counter(cnt, temp_list)
    print(cnt)
def test_file():
    cnt = get_counter()
    temp_path = 'c:\\temp.txt'
    temp_str = get_file_str(temp_path)
    temp_list = str_to_list(temp_str)
    cnt = counter(cnt, temp_list)
    print(cnt)
def main():
    test_str()
    print('#' * 50)
    test_file()
if __name__ == '__main__':
    main()
