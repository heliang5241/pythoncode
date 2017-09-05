f = open("config.txt")
content_list = f.readlines()
for line in content_list:
    weifuwu_name = line.split("|")[0]
    port = line.split("|")[1].split('\n')[0]
    path = "/tmp/" + weifuwu_name + "_" + port +".txt"
    url = "http://127.0.0.1:" + port + "/health"
    print url
    print path
f.close()