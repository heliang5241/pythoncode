import os
# cmd = 'curl http://192.168.28.12:8911/health'
# str1 = os.system(cmd)
# str = str(str1)
# list = str.split('"')

# str ='{"description":"Remote status from Eureka server","status":"DOWN","discoveryComposite":{"description":"Remote status from Eureka server","status":"DOWN","discoveryClient":{"description":"Spring Cloud Eureka Discovery Client","status":"UP","services":["yj_ymjh_apigateway","taskv1","kidv1","facadev1","eureka","user","yp-custody"]},"eureka":{"description":"Remote status from Eureka server","status":"DOWN","applications":{"YJ_YMJH_APIGATEWAY":1,"TASKV1":1,"KIDV1":1,"DYNAMICSV1":0,"FACADEV1":1,"EUREKA":2,"USER":1,"YP-CUSTODY":1}}},"diskSpace":{"status":"UP","total":44634951680,"free":39233200128,"threshold":10485760},"mongo":{"status":"DOWN","error":"org.springframework.dao.DataAccessResourceFailureException: Timed out after 30000 ms while waiting for a server that matches ReadPreferenceServerSelector{readPreference=primary}. Client view of cluster state is {type=REPLICA_SET, servers=[{address=alirwtmangodb01.yumijihua.com:3717, type=UNKNOWN, state=CONNECTING, exception={com.mongodb.MongoSocketOpenException: Exception opening socket}, caused by {java.net.NoRouteToHostException: No route to host (Host unreachable)}}, {address=alirwtmangodb02.yumijihua.com:3717, type=UNKNOWN, state=CONNECTING, exception={com.mongodb.MongoSocketOpenException: Exception opening socket}, caused by {java.net.NoRouteToHostException: No route to host (Host unreachable)}}]; nested exception is com.mongodb.MongoTimeoutException: Timed out after 30000 ms while waiting for a server that matches ReadPreferenceServerSelector{readPreference=primary}. Client view of cluster state is {type=REPLICA_SET, servers=[{address=alirwtmangodb01.yumijihua.com:3717, type=UNKNOWN, state=CONNECTING, exception={com.mongodb.MongoSocketOpenException: Exception opening socket}, caused by {java.net.NoRouteToHostException: No route to host (Host unreachable)}}, {address=alirwtmangodb02.yumijihua.com:3717, type=UNKNOWN, state=CONNECTING, exception={com.mongodb.MongoSocketOpenException: Exception opening socket}, caused by {java.net.NoRouteToHostException: No route to host (Host unreachable)}}]"},"refreshScope":{"status":"UP"},"hystrix":{"status":"UP"}}'
str = os.popen('curl http://192.168.28.12:8911/health').readlines()
list = str.split('"')
key = ''
values = ''
for i in range(len(list)):
    if list[i] == 'status' and list[i + 1] == ':':
        key = list[i - 2]
        values = list[i + 2]
        print key, values