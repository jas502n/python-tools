# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 下午12:00
# @Author  : MyPuppet
# @File    : search.py
# @Software: PyCharm
import sys
import random
import requests as req
from urllib import parse
from lxml import etree
from multiprocessing import Pool

BASE_URL = 'http://www.ygdy8.com'
SEARCH_URL = 'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&pagesize=1000&keyword='


# 关键字需要URL字符编码
def get_headers():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
        'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
        'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
    ]
    ua = random.choice(user_agent_list)
    headers = {'User-Agent': ua}
    return headers


def search(keyword):
    keyword = parse.quote(keyword.encode("gbk"))
    url = SEARCH_URL + keyword
    res = req.get(url, headers=get_headers())
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.text)
    tags = html.xpath('//div[@class="co_content8"]/ul//a')
    result_urls = []
    for tag in tags:
        url = BASE_URL + tag.get('href')
        result_urls.append(url)
    return result_urls


def parse_html(url):
    res = req.get(url, headers=get_headers())
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.text)
    title = html.xpath('//div[@class="bd3r"]//div[@class="title_all"]/h1/font')[0].text
    downloads = html.xpath('//div[@id="Zoom"]//table//a/@href')
    print('[%s]' % title)
    for download in downloads:
        print('[下载链接] [%s]' % download)
    print('\n|----------------------------------------------------------|\n')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python %s movie_name" % sys.argv[0])
        exit(-1)
    urls = search(sys.argv[1])
    pool = Pool()
    pool.map(parse_html, urls)