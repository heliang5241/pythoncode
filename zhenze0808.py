import re
f = open("gethtml.txt",'r')
list = f.read().split("\n")
for i in range(len(list)):
    reg = r'172.20'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,list[i])
    if imglist:
        print list[i]
f.close()