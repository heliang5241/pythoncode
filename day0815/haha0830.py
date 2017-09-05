import urllib2
import os
import sys
port = sys.argv[1]
filename = sys.argv[2]

url = "http://192.168.29.12:" + port + "/health"
r = urllib2.Request(url)
path = "/tmp/" + filename + port + ".txt"
cmd = 'cat /dev/null>' + path
try:
        f = urllib2.urlopen(r, data=None, timeout=3)
        str1 = f.read()
        str = str(str1)
        list = str.split('"')
        key = ''
        values = ''
        os.system(cmd)
        for i in range(len(list)):
            if list[i] == 'status' and list[i + 1] == ':':
                with open(path, 'a+w') as f:
                    key = list[i - 2]
                    values = list[i + 2]
                    print key, values
                    f.write(key + ' ')
                    f.write(values + '\n')
                    f.flush
        f.close
except Exception,e:
        os.system(cmd)
        print str(e)
