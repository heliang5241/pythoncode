import urllib
import re
def getHtml(html):
    page = urllib.urlopen(html)
    haha = page.read()
    return haha
def getImg(html):
    reg = r'src="(.*?\jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        print imgurl

if __name__ == '__main__':
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&p=1'
    zz = getHtml(url)
    getImg(zz)



