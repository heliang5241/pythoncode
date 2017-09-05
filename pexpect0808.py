#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2017/8/8 9:23
# @Author  : heliang
import pexpect
child = pexpect.spawn('ssh 192.168.1.23')
fout = file('mylog.txt','w')
child.logfile = fout

child.expect("password:")
child.sendline("123456")

child.expect("#")
child.sendline("ifconfig")
child.expect("#")
for i in range()





