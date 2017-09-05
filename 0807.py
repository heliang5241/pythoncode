#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/7 9:32
# @Author  : heliang
import sys
import time
def Stdin0807():
    sys.stdin = open("iplist.txt","r")
    for line in sys.stdin.readlines():
        print line

def Read0807():
    f = open("iplist.txt","r")
    print f.read()
    f.close()
def Stdout0807():
    sys.stdout = open(r"./iplist.txt","a")
    print ("goodbye")
    sys.stdout.close()
if __name__ == '__main__':
    # Stdin0807()
    # Read0807()
    Stdout0807()