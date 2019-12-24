# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:21:12 2019

@author: AntikoFang
"""
# 福利词云图
from pyecharts import WordCloud
import jieba
#导入文本
txt = open(r'D:\BI大屏\txt文件\优惠.txt',encoding = 'utf-8').read()

  # 导入停用词
jieba.load_userdict(r'D:\BI大屏\txt文件\停用词.txt')
#分词
cun=jieba.cut(txt)
#读取停用词文件
stops=open(r'D:\BI大屏\txt文件\去停用词.txt','r',encoding='UTF-8').read()
# 去停用词
tokens=[token for token in cun if token not in stops]
d={}
for i in tokens:
    d[i] = d.get(i,0) + 1

count_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
count_list = count_list[:25]
keyword_list = [k[0] for k in count_list]
value_list = [k[1] for k in count_list]

wordcloud = WordCloud(width=600,height=500)
wordcloud.add('',keyword_list,value_list,word_size_range=[20,100])
#wordcloud.use_theme("dark")   
wordcloud.render(r"D:\BI大屏\统计学招聘报告\福利词云图.html")

#==============================================================================

# 职位类别词云图
from pyecharts import WordCloud
import jieba
#导入文本
txt = open(r'D:\BI大屏\txt文件\职能类别.txt',encoding = 'utf-8').read()

  # 导入停用词
jieba.load_userdict(r'D:\BI大屏\txt文件\停用词.txt')
#分词
cun=jieba.cut(txt)
#读取停用词文件
stops=open(r'D:\BI大屏\txt文件\去停用词.txt','r',encoding='UTF-8').read()
# 去停用词
tokens=[token for token in cun if token not in stops]
d={}
for i in tokens:
    d[i] = d.get(i,0) + 1

count_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
count_list = count_list[:25]
keyword_list = [k[0] for k in count_list]
value_list = [k[1] for k in count_list]

wordcloud = WordCloud(width=600,height=500)
wordcloud.add('',keyword_list,value_list,word_size_range=[20,100])
#wordcloud.use_theme("dark")   
wordcloud.render(r"D:\BI大屏\统计学招聘报告\职能类别词云图.html")