f = open("/root/shell/url.txt")
line = f.readline()
while line:
    print line
    line = f.readline()