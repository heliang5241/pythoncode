import urllib2
import socket
# socket.setdefaulttimeout(40)

str1 = '{"description":"Spring Cloud Eureka Discovery Client","status":"UP","discoveryComposite":' \
      '{"description":"Spring Cloud Eureka Discovery Client","status":"UP","discoveryClient":' \
      '{"description":"Spring Cloud Eureka Discovery Client","status":"UP","services":["eurek' \
      'a-yinpiao-test","kidv1","inituserconsumer","dynamicsconsumerv1","dynamicsv1","yp-intelli' \
      'gence-provider.sms","cashbookv1","growthv1","authimagev1","yp-intelligence-provider.inform' \
      'ation","wechatjobv1","innerapigateway","yp-intelligence-gateway.server","growthjobv1","inform' \
      'ationv1","user","apigateway","yp-mobiledata-job","taskv1","yp-intelligence-gateway","yp-partn' \
      'er-job","taskconsumerv1","yp-intelligence-provider.user","facadev1","yp-partner","eureka-yu' \
      'mijihua-test","kidconsumerv1","yp-intelligence-provider.huifu","yp-custody"]},"eureka":{"des' \
      'cription":"Remote status from Eureka server","status":"UP","applications":{"EUREKA-YINPIAO' \
      '-TEST":1,"KIDV1":1,"INITUSERCONSUMER":1,"DYNAMICSCONSUMERV1":1,"YP-MOBILEDATA":0,"DYNAMICSV' \
      '1":1,"YP-INTELLIGENCE-PROVIDER.SMS":1,"YINPIAO-UAT":0,"MICROSERVICE-PROVIDER-USER":0,"CASHB' \
      'OOKV1":1,"GROWTHV1":1,"AUTHIMAGEV1":1,"YP-INTELLIGENCE-PROVIDER.HUIFU":1,"YP-INTELLIGENCE-PR' \
      'OVIDER.INFORMATION":1,"MICROSERVICE-GATEWAY-ZUUL":0,"WECHATJOBV1":1,"INNERAPIGATEWAY":1,"YJ_Y' \
      'MJH_APIGATEWAY":0,"YP-INTELLIGENCE-GATEWAY.SERVER":1,"GROWTHJOBV1":1,"YP-INTELLIGENCE-AGENT.RE' \
      'ST":0,"INFORMATIONV1":1,"USER":1,"APIGATEWAY":1,"YP-MOBILEDATA-JOB":1,"TASKV1":1,"YP-INTELLI' \
      'GENCE-GATEWAY":3,"YP-PARTNER-JOB":1,"TASKCONSUMERV1":1,"YP-INTELLIGENCE-PROVIDER.USER":1,"FACAD' \
      'EV1":1,"YP-PARTNER":1,"EUREKA-YUMIJIHUA-TEST":1,"KIDCONSUMERV1":1,"YP-CUSTODY":1}}},"diskSpac' \
      'e":{"status":"UP","total":44634951680,"free":36173520896,"threshold":10485760},"refreshSco' \
      'pe":{"status":"UP"},"hystrix":{"status":"UP"}}'
# socket.setdefaulttimeout(40)
# urllib2.socket.setdefaulttimeout(40)
req = urllib2.Request('http://192.168.28.12:8911/health')
# req = urllib2.Request('http://192.168.11.62:8902/health')
try:
        print 1
        # response = urllib2.urlopen(req, data=None, timeout=3000)
        response = urllib2.urlopen(req,timeout = 600)
        print 2
        str = response.read()
        list = str.split('"')
        key = ''
        values = ''
        for i in range(len(list)):
            if list[i] == 'status' and list[i + 1] == ':':
                key = list[i - 2]
                values = list[i + 2]
                print key, values

except Exception,e:
        print str(e)


