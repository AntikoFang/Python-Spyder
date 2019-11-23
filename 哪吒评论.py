# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:23:46 2019

@author: Administrator
"""

#from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://movie.douban.com/subject/26794435/comments?status=P"

def GetUrl(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    return BeautifulSoup(req.text,'lxml')

bs = GetUrl("https://movie.douban.com/subject/26794435/comments?status=P")

# 评论内容
ContentList = bs.find('div',{'id':'comments'}).find_all('span',{'class':'short'})
content = []

for contents in ContentList:
    content.append(contents.get_text())

# 评论者
NameList = bs.find_all('span',{'class':'comment-info'})
name = []

for names in NameList:
    name.append(names.get_text())

# 评论时间
TimeList = bs.find_all('span',{'class':'comment-time'})
time = []

for times in TimeList:
    time.append(times.get_text())

VoteList = bs.find('span',{'class':'comment-vote'})
vote = []

for votes in VoteList:
    vote.append(votes.get_text())


# 汇总
df = pd.DataFrame([content,time,vote],index = ['评论内容','评论时间','点赞数'],columns = name)






