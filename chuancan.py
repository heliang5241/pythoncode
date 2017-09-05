import sys,os
def Yp():
    javapid = os.popen("ps -ef|grep yp-intelligence-agent.rest-1.0.jar|grep -v grep|awk '{print $2}'").read()
    return int(javapid)

def Ag():
    javapid = os.popen("ps -ef|grep authimg.jar|grep -v grep|awk '{print $2}'").read()
    return int(javapid)
def Cn():
    javapid = os.popen("ps -ef|grep coupon.jar|grep -v grep|awk '{print $2}'").read()
    return int(javapid)
def numbers_to_strings(argument):
    switcher = {
        "yp": Yp(),
        "ag": Ag(),
        "cn": Cn(),
    }
    return switcher.get(argument, "nothing")

if __name__ == '__main__':
    print numbers_to_strings(sys.argv[1])
