 # -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:09:38 2019

@author: AntikoFang
"""

import re
from lxml import etree
from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests



class Content:
    
    def __init__(self,url):
        self.url = url
    
    # 解析网页函数
    def GetPage(self,url):
        req = requests.get(url)
        req.encoding = 'utf-8'
        return BeautifulSoup(req.text,'lxml')
    
    # 网页标题函数
    def UrlTitle(self,url):
        bs = self.GetPage(url)
        title = bs.find('title').text
        print('网页标题:',title)
    
    # 网址链接函数
    def Url(self,url1, attr, attr1, attr2):
        urls = []
        bs = self.GetPage(url1)
        # 找到网页面板所有链接
        Urls = bs.find(attr,{attr1:attr2}).find_all('a')     #找到所有a标签
        for items in Urls:
            urls.append(items.get("href"))                   # 找到href属性
        #urls.add('http://xgxy.hbue.edu.cn'+items.get("href"))
        # str(College.College_Url(self,a))+
        #print(urls)
        return(urls)
    
class College:

    def __init__(self,url):
        self.url = url
    
    # 解析网页函数
    def GetPage(self,url):
        req = requests.get(url)
        req.encoding = 'utf-8'
        return BeautifulSoup(req.text,'lxml')
    
    # 获取某学院网页面板所有链接
    def College_Url(self,a,attr, attr1, attr2):
        # 获得所有学院链接
        college_urls = Content.Url(self,url,'li','class','menu-item i2')[1:]
        
        urls = []
        # 进入其中一个学院
        bs = self.GetPage(college_urls[a])
        print('学院链接：{}'.format(college_urls[a]))
        # 找到学院网页面板中所有链接
        Urls = bs.find(attr, {attr1: attr2}).find_all('a')  # 找到所有a标签
        for items in Urls:
            urls.append(college_urls[a]+items.get("href"))
        #print(items.get("href"))
        
        #    for items in Urls:
        #        urls.append(college_urls[j] + items.get("href"))
            #urls.append('http://jrxy.hbue.edu.cn/'+items.get("href"))  # 找到href属性
        return urls
        #print(urls)
        
    # 进入学院面板链接获取内容
    def body(self,a,attr, attr1, attr2):
        urls = self.College_Url(a,attr, attr1, attr2)
        
        for item in urls:
            bs = self.GetPage(item)
            title = bs.find('h1',{'class':'arti_title'}).text  
            print(title)
            #print('{}标题'.format(),title)
            content = bs.find('div',{'class':'wp_articlecontent'}).text
            #print('{}内容\n'.format(),content)
            print(content)
        
        #urls = Content.Url(self,1,college_url, 'div', 'id', 'wp_news_w6')
        #print(urls)

# 湖北经济学院官网链接地址
url = 'http://www.hbue.edu.cn/'
#content1 = Content(url)
# 金融学院
college = College(url)
print("学院新闻")
college.body(1,'div','id','wp_news_w6')
print("教学动态")
college.body(1,'div','id','wp_news_w8')
print("学术动态")
college.body(1,'div','id','wp_news_w9')
print("学工动态")
college.body(1,'div','id','wp_news_w10')
print("就业信息")
college.body(1,'div','id','wp_news_w11')

#college.All_Url(url, 'div', 'id', 'wp_news_w6')
#college.body(college_url, 'div', 'id', 'wp_news_w6')