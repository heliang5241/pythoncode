import urllib2
r = urllib2.Request("http://192.168.28.12:8911/health")
try:
        print 1
        f = urllib2.urlopen(r, data=None, timeout=3000)
        print 2
        result = f.read()
        print 3
except Exception,e:
        print str(e)

print 5