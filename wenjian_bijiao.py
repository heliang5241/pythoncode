#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2017/8/7 18:17
# @Author  : heliang
import difflib
import sys
a = open('defines.inc.php', 'U').readlines()
b = open('defines.inc2.php', 'U').readlines()
diff = difflib.ndiff(a, b)

print sys.stdout.writelines(diff)


