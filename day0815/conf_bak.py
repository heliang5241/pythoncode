#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 15:32
# @Author  : heliang
import urllib2
cf = open("config.txt")
conf_list = cf.readlines()
for i in range(len(conf_list)):
    weifuwu_name = conf_list[i].split("|")[0]
    port = conf_list[i].split("|")[1].split('\n')[0]
    listStr = ['http://127.0.0.1:','port','/health']
    print url
    r = urllib2.Request(url)
    path = "/tmp/" + weifuwu_name + "_" + port + ".txt"
    cmd = "cat /dev/null>" + path
    # print path
    # try:
    #     f = urllib2.urlopen(r, data=None, timeout=3)
    #     str1 = f.read()
    #     str2 = str(str1)
    #     list = str2.split('"')
    #     key = ''
    #     values = ''
    #     os.system(cmd)
    #     for i in range(len(list)):
    #         if list[i] == 'status' and list[i + 1] == ':':
    #             with open(path, 'a+w') as fe:
    #                 key = list[i - 2]
    #                 values = list[i + 2]
    #                 print key, values
    #                 fe.write(key + ' ')
    #                 fe.write(values + '\n')
    #                 fe.flush()
    #             fe.close()
    # except Exception, e:
    #     os.system(cmd)
    #     print str(e)
cf.close()
