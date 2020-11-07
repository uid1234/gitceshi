import requests
from bs4 import BeautifulSoup
import bs4
import time

def getHTMLText(url):
    kv = {"user-agent":"Mozilla/5.0"}
    try:
        r = requests.get(url,headers=kv,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败！")
        return ""


def getMovieInfo(html,ulist):
    soup = BeautifulSoup(html,"html.parser")
    for td in soup.find('ol').children:
        if isinstance(td,bs4.element.Tag):
            trs = td('span')
            ulist.append(trs[0].string)
    time.sleep(1)

def printMovieInfo(ulist):
    for lit in ulist:
        print("{0:{1}^10}".format(lit,chr(12288)))

    
def main():
    start_url = "https://movie.douban.com/top250?start="
    ulist = []
    path = 10
    for i in range(path):
        url = start_url+str(i*25)
        html = getHTMLText(url)
        getMovieInfo(html,ulist)
    print("豆瓣top250排名：")
    printMovieInfo(ulist)

main()

