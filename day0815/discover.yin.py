#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/5 15:31
# @Author  : qq:1960050004
import urllib
import urllib2
url = "http://discover.yinpiao.com/"
str = urllib.urlopen(url)
print str.readlines
