#!/usr/bin/env python  
# coding: utf-8    
# Author  : gogit2194
# Datetime: 20170705
from __future__ import unicode_literals
import requests
import re
import time
import os


#agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
def html_resolve(url):
    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    headers = {'User-Agent': agent,
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Content-type": "test/html"}
    r = requests.get(url , headers=headers)
    r.encoding = "gbk"
    #print (r.text)
    ss = r.text
    return ss
def pages_n(ss):
    #获取页数
    urls_pages=re.compile(r"[\u5171]\d{2}")
    p =  urls_pages.search(ss,0)
    pages = p.group()
    #替换共字为空白 得到页数
    img_pages = re.sub(r"[\u5171]",'',pages)
    int(img_pages)
    return img_pages
def img_url(ss):
    #获取图片地址并加入下载列表
    urls=re.findall(r"newkuku.*?\.jpg",ss,re.I)
    #print (urls)
    return urls[0]
    #url_img = "http://n.1whour.com/" + img[n]
    #获取共后面的数字 （页数）

def down_img(img_url,dir_path,img_name):
    filename = os.path.join(dir_path,img_name)
    try:
        res = requests.get(img_url,timeout=60)
        if str(res.status_code)[0] == '4':
            print(str(res.status_code),":",img_url)
            return False
    except Exception as e:
        print('出现错误',img_url)
        print(e)
        return False
    with open(filename+'.jpg','wb') as f:
        f.write(res.content)
    return True

def mkdir(dir_name):
    dir_path = os.path.join(dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path
if __name__ == '__main__':
    urls_comic =[]
    urls_total = []
    urls_img = []
    url = "http://comic2.kukudm.com/comiclist/1953/38891/1.htm"
    ss = html_resolve(url)
    pages = pages_n(ss)
    x = int (pages)
    #链接重新组合好插入变量已输出每一集的所有页面链接
    urls = url
    print("共 %s 页" % x)
    for i in range(1,x+1):
        u = re.sub(r'1.htm', '', urls) + str(i) + '.htm'
        #print u
        #return u
        time.sleep(0.2)
        urls_total.append(u)
    #print urls_total[31]
    #解析当前集数的所有网页提取下载地址
    pa = 0
    for f in range(0,x):
        pa += 1
        d = urls_total[f]
        time.sleep(0.2)
        img = html_resolve(d)
        g = img_url(img)
        h = "http://n.1whour.com/" + g
        urls_img.append(h)
        print("已解析第 %s 页" % pa)
    #建立单集文件夹

    #下载
    dir = './image/'
    dir_path = mkdir(dir)
    index = 0
    for l in urls_img:
        if down_img(l, dir_path, str(index)):
            index += 1
            time.sleep(0.2)
            print("已下载第 %s 张" % index)