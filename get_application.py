import os
import sys
import re
str ='''AUTHIMAGEV1
DYNAMICSCONSUMERV1
DYNAMICSV1
EUREKA-YINPIAO-TEST
EUREKA-YUMIJIHUA-TEST
FACADEV1
GROWTHJOBV1
GROWTHV1
INFORMATIONV1
INITUSERCONSUMER
INNERAPIGATEWAY
KIDCONSUMERV1
KIDV1
TASKCONSUMERV1
TASKV1
USER
WECHATJOBV1
YJ_YMJH_APIGATEWAY
'''
list = str.split()
# print list
for i in range(len(list)):
    reg = r'[^D]'
    str2 = re.findall(reg,list[i])
    print str2


