import os
# cmd = 'curl http://192.168.28.12:8911/health'
# str1 = os.system(cmd)
# str = str(str1)
# list = str.split('"')
# httpcode = os.system('curl -I -m 10 -o /dev/null -s -w %{http_code}  http://192.168.28.12:8911/info')
# os.system('cat /dev/null>/etc/zabbix/scripts/tmp.txt')
os.popen('cat /dev/null>/etc/zabbix/scripts/result')
os.popen('wget http://192.168.29.21:8920/health -O /etc/zabbix/scripts/result')
str1 = open('result').readline()
# os.popen('rm -rf /etc/zabbix/scripts/result')
#str1 = os.popen('curl -s http://172.17.0.15:8903/health').readlines()
str = str(str1)
list = str.split('"')
key = ''
values = ''
os.system('cat /dev/null>/etc/zabbix/scripts/tmp.txt')
for i in range(len(list)):
    if list[i] == 'status' and list[i + 1] == ':':
        with open('/etc/zabbix/scripts/tmp.txt', 'a+w') as f:
            key = list[i - 2]
            values = list[i + 2]
            print key,values
            f.write(key + ' ')
            f.write(values + '\n')
            f.flush
        f.close