import urllib2
import os
r = urllib2.Request("http://192.168.29.29:8916/health")
try:
        print 1
        f = urllib2.urlopen(r, data=None, timeout=3)
        print 2
        str1 = f.read()
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
                    print key, values
                    f.write(key + ' ')
                    f.write(values + '\n')
                    f.flush
                f.close
        print 3
except Exception,e:
        os.system('cat /dev/null>/etc/zabbix/scripts/tmp.txt')
        print str(e)
# print 5
