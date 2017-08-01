import os
# cmd = 'curl http://192.168.28.12:8911/health'
# str1 = os.system(cmd)
# str = str(str1)
# list = str.split('"')
httpcode = os.system('curl -I -m 10 -o /dev/null -s -w %{http_code}  http://192.168.28.12:8911/info')
str1 = os.popen('curl -s http://192.168.28.12:8911/health').readlines()
#print str1
str = str(str1)
#print type(str)
list = str.split('"')
key = ''
values = ''
for i in range(len(list)):
    if list[i] == 'status' and list[i + 1] == ':':
        key = list[i - 2]
        values = list[i + 2]
        print key, values