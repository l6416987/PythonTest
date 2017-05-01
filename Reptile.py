#congig=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" alt'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imaurl in imglist:
        urllib.urlretrieve(imaurl, '%s.jpg' % x)
        x += 1

 # src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1494085500&amp;di=53a9db5bb33238c32dec917f41ca4fb3&amp;imgtype=jpg&amp;er=1&amp;src=http%3A%2F%2Fwww.sinaimg.cn%2Fqc%2Fautoimg%2Fcar%2F02%2F63%2F129646302_950.jpg" data-clicktime="" data-israndom="" data-isala="1" style="display: none;">

html = getHtml('http://sports.qq.com/nba/')
print getImg(html)
