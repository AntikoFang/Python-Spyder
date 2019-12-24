# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:50:21 2019

@author: AntikoFang
"""
# 技能雷达图

from pyecharts import Radar

skill = ['python','SQL','数据分析','linux','数据挖掘','SAP','算法','NLP','数据统计','AP','深度学习','excel']
num = [[308,314,1012,77,305,25,390,30,242,118,81,590]]
num1 = [700,700,800,400,700,200,700,200,700,700,200,700]
sch = zip(skill,num1)
schema = [s for s in sch]

radar = Radar('技能分布雷达图',title_pos = 'center')
radar.config(schema)
radar.add('',num, is_area_show = True,area_color = 'blue',is_splitline_show=True,is_axisline_show=True)
#radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,legend_selectedmode='single')
radar.render(r'D:\BI大屏\统计学招聘\技能雷达图.html')


skill = ['python','SQL','数据分析','linux','数据挖掘','SAP','算法','NLP','数据统计','AP','深度学习','excel']
num = [[13721,13030,11044,14800,13337,8625,14219,18892,8601,13565,19477,8492]]
num1 = [20000,20000,20000,20000,20000,20000,20000,20000,20000,20000,20000,20000]
sch = zip(skill,num1)
schema = [s for s in sch]
radar = Radar('技能薪资雷达图',title_pos = 'center')
radar.config(schema)
radar.add('',num, is_area_show = True,area_color = 'blue',is_splitline_show=True,is_axisline_show=True)
#radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,legend_selectedmode='single')
radar.render(r'D:\BI大屏\统计学招聘\技能薪资雷达图.html')
