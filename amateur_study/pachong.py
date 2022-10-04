# import bs4  # 解析网页数据获取
import urllib.request, urllib.error  # 指定URL爬取网页数据


def askURL():
    url = "https://music.163.com/#/discover/toplist?id=3778678"  # 要爬取网页的url
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"}
    req = urllib.request.Request(url,headers=head)    # 模拟浏览器
    html = ""
    try:
        resp = urllib.request.urlopen(req)    # 爬取网页内容
        html = resp.read().decode("UTF-8")    # 对爬取结果解码
        print(html)
    except urllib.error.URLError as e:    # 抛出可能出现的异常：url找不到
        if hasattr(e, "reason"):
            print(e.reason)    # 打印异常信息

askURL()
