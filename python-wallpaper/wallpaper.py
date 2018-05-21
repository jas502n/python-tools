#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# 替换成1920x1080
# https://images.wallpaperscraft.com/image/skier_mountains_snow_121238_300x168.jpg
# https://images.wallpaperscraft.com/image/skier_mountains_snow_121238_1920x1080.jpg
'''

# coding=utf-8
import urllib
import re


# 定义函数getHtml，获取网站源码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print 'Downloading: %.2f%%' % per


# 定义函数getImg，获取图片列表地址
def getImg(html,y):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 1
    for imgurl in imglist:
        newimgurl = list(imgurl)
        newimgurl[-11:] = list('1920x1080.jpg')
        s = ''.join(newimgurl)
        print '''******************************************************\n
************                              ************\n
************   Download JPG  %s-%s.jpg     ************\n
************                              ************\n
******************************************************\n
                ''' % (y,x)
        urllib.urlretrieve(s, '%s-%s.jpg' % (y, x), cbk)
        x += 1

for y in range(1,3):
    url = 'https://wallpaperscraft.com/all/page%s' % y
    print url
    html = getHtml(url)
    getImg(html,y)




