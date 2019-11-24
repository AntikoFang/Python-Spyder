# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:56:24 2019

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
            if items.get("href")[0] == '/':
                urls.append('http://xgxy.hbue.edu.cn'+items.get("href"))
            else:
                urls.append(items.get("href"))
                   # 找到href属性
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
        # 获得所有学院官网链接
        college_urls = Content.Url(self,url,'li','class','menu-item i2')[1:]
        urls =[]
        # 进入其中一个学院
        bs = self.GetPage(college_urls[a])
        print('学院链接：{}'.format(college_urls[a]))
        # 找到学院网页其中一个面板中所有的链接
        Urls = bs.find(attr, {attr1: attr2}).find_all('a')  # 找到所有a标签
        for items in Urls:
            urls.append(college_urls[a][:-1]+items.get("href")) # 获取href属性添加后缀
            return urls
            #print(urls)
        #print(items.get("href"))
        #return urls
        
    # 进入面板获取所有链接
    def body(self,a,attr, attr1, attr2):
        # 进入面板(点击更多按钮)
        url = self.College_Url(a,attr, attr1, attr2)
        bs = self.GetPage(url[0])
        #self.GetPage('http://xgxy.hbue.edu.cn/2627/list.htm')
        
        # 获取面板所有链接
            #翻页
        Pages = int(bs.find('em',{'class':'all_pages'}).text)
        for i in range(1,Pages):
            body_urls = Content.Url(self, 'http://xgxy.hbue.edu.cn/2627/list{}.htm'.format(i),'div', 'id', 'wp_news_w6')
            if i == 2:
                body_urls = body_urls[2:]
            for items in body_urls:
                bs = self.GetPage(items)
                
                #判断是否为2019年
                a = bs.find('span',{'class':'arti_update'}).text
                if '2019' in a:
                    title = bs.find('h1',{'class':'arti_title'}).text  
                    print(title)
                    #print('{}标题'.format(),title)
                    content = bs.find('div',{'class':'wp_articlecontent'}).text
                    #print('{}内容\n'.format(),content)
                    print(content)
                else:
                    break
           
            
               
    #urls = Content.Url(self,1,college_url, 'div', 'id', 'wp_news_w6')
    #print(urls)

# 湖北经济学院官网链接地址
url = 'http://www.hbue.edu.cn/'
#content1 = Content(url)
# 金融学院
college = College(url)
print("综合新闻")
#点击综合新闻中的更多按钮获取内容
content = college.body(6,'div','class','more_btn')

#college.College_Url(6,'div','class','more_btn')
#college.GetPage(college.College_Url(6,'div','class','more_btn')[0])
#college.All_Url(url, 'div', 'id', 'wp_news_w6')
#college.body(college_url, 'div', 'id', 'wp_news_w6')

#content = Content(url)
#for i in range(1,4):
#    url_list = content.Url('http://xgxy.hbue.edu.cn/2627/list{}.htm'.format(i),'ul', 'class', 'wp_article_list')








