
list = ['http://192.168.29.12:8183/health', 'http://192.168.29.16:8929/health', 'http://192.168.29.11:8911/health', 'http://192.168.29.21:8920/health', 'http://192.168.29.18:8928/health', 'http://192.168.29.13:8912/health', 'http://192.168.29.17:8933/health', 'http://192.168.29.10:8913/health', 'http://192.168.29.24:8181/health', 'http://192.168.29.22:8902/health', 'http://192.168.11.20:8810/health', 'http://192.168.11.20:8111/health', 'http://192.168.11.20:8112/health', 'http://192.168.11.20:8804/health', 'http://192.168.11.20:8119/health', 'http://192.168.11.20:8805/health', 'http://192.168.11.20:8803/health', 'http://192.168.11.20:8113/health', 'http://192.168.29.72:8088/health', 'http://192.168.29.70:8806/health']
r = open('d://0801.txt','w')
for i in range(0,len(list)):
    # print list[i]
    str = list[i].split('/')[2]
    ip = str.split(':')[0]
    port = str.split(':')[1]
    str = ip + ' '+'ip='+ip + ' '+'port='+port
    r.write(str)
    r.write('\r')
    print str
r.close()

    # print str1,str2
