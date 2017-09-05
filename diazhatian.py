#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2017/8/7 20:21
# @Author  : heliang
import sys,os
javapid = os.popen("ps -ef|grep yp-intelligence-agent.rest-1.0.jar|grep -v grep|awk '{print $2}'").read()
print javapid

