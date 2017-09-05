import urllib
import re
import urllib2
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
ok_list = []
bad_list = []
def getImg(html):
    reg = r'a href="(.*?\info)"'
    urlre = re.compile(reg)
    urllist = re.findall(urlre,html)
    for imgurl in urllist:
        new_url = imgurl.split('info')[0]
        new_url2 = new_url + 'health'
        # s1 = new_url.split('//')[1].split(':')[0]
        r = urllib2.Request(new_url2)
        try:
            # print 1
            f = urllib2.urlopen(r, data=None, timeout=10)
            # print 2
            # result = f.read()
            ok_list.append(new_url2)
            # print 3
        except Exception, e:
            # print str(e)
            bad_list.append(new_url2)

        # print 5
html = getHtml("http://testdiscover.yumijihua.com/")
getImg(html)
# ok_str = str(ok_list)
print ok_list
print bad_list

