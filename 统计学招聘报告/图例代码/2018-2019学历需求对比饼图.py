# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:28:06 2019

@author: Administrator
"""

# 2018-2019学历需求对比饼图
#=============================================================================
import jieba
#导入文本
txt = open(r'D:\BI大屏\txt文件\学历.txt',encoding = 'utf-8').read()
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
count_list = count_list[:20]
keyword_list = [k[0] for k in count_list]
value_list = [k[1] for k in count_list]

from pyecharts import Pie
attr1 = keyword_list[:-1]
v1 = value_list[:-1]
attr2 = ['大专','本科','硕士','博士','不限']
v2 = [40,549,46,7,89]

#v2 = [19, 21, 32, 20, 20, 33]
pie =Pie("2018-2019学历需求对比图", title_pos='center', width=900)
# pie.use_theme('dark')

pie.add("2018", attr2, v2, is_random=True, radius=[20, 45],is_legend_show=True,is_label_show=True)#rosetype='radius'
pie.add("2019", attr1, v1, is_random=True, radius=[50, 70], is_legend_show=False, is_label_show=True)
# pie.show_config() 
pie.render(r"D:\BI大屏\统计学招聘报告\2018-2019学历需求饼图对比.html")