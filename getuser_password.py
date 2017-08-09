import pexpect,os
f = open("iplist.txt","r")
str = f.readline()
os.system("cat /dev/null>/mnt/mylog.txt")
while str:
    ip = 'ssh' + ' ' + str.split()[0]
    child = pexpect.spawn(ip)
    fout = file('mylog.txt', 'a+')
    child.logfile = fout

    child.expect("password:")
    child.sendline(str.split()[1])

    child.expect("#")
    child.sendline("ifconfig")
    child.expect("#")
    str = f.readline()
f.close()

