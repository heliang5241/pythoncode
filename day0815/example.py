#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 7:17
# @Author  : heliang
import os
import sys
import linecache
leixing = sys.argv[1]
canshu = sys.argv[2]
def Send_Received_packs(leixing,num):
    send_cmd = "snmpwalk -v 2c -c yinpiao 172.20.1.2 .1.3.6.1.4.1.28557.2.3.2.3.1." + leixing + "|awk "
    tmp_txt = "/tmp/firewall/result" + leixing + ".txt"
    if leixing =="11":
        # print "this is 11"
        tmp_txt2 = "/tmp/firewall/send.txt"
    else:
        # print "this is 4"
        tmp_txt2 = "/tmp/firewall/received.txt"
    # print tmp_txt2
    theline = linecache.getline(tmp_txt2,int(num))
    # print int(theline)
    send_cmd2 = send_cmd + "'{if(NR==" + num + ") print $4}'"
    str1 = os.popen(send_cmd2).readlines()[0]
    # print int(str1)
    result = int(str1)-int(theline)
    print result

if __name__ == '__main__':
    Send_Received_packs(leixing,canshu)