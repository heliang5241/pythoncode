import re
import urllib
def gethtml(url):
    ht =urllib.urlopen(url)
    str = ht.read()
    return str

url = 'http://www.cnblogs.com/ahwwmb/archive/2013/03/12/2955678.html'
# print gethtml(url)
reg = r'a href="(.*?\tar.gz)"'
targz = re.compile(reg)
targzlist = targz.findall(gethtml(url),reg)
for lists in targzlist:
    print lists
