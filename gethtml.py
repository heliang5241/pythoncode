import urllib,re
def GetHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def GetUrl(html):
    reg = r'a href="(.*?\info)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    f = open("gethtml.txt", "w+")
    for imgurl in imglist:
        new_url = (imgurl.split('info')[0])
        f.write(new_url)
        f.write("\n")
        print new_url
    f.close()
if __name__ == '__main__':
    urls = GetHtml("http://discover.yinpiao.com/")
    GetUrl(urls)








