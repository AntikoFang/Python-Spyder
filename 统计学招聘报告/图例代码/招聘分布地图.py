# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:37:31 2019

@author: AntikoFang
"""

from pyecharts import Map

attr2 = ['北京','上海','陕西','浙江','湖北','四川','重庆','湖南','广东','江苏','安徽','福建',
         '河南','山东','河北','辽宁','甘肃']
value2 = [193,122,6,72,18,26,1,8,107,8,7,4,5,3,3,1,1]

map = Map("2018统计学数据分析岗位招聘分布", width=1200, height=600,title_pos="center")
map.add(
    "",
    attr2,
    value2,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
    is_label_show=True
)
map.render(r'D:\BI大屏\统计学招聘报告\2018招聘分布地图.html')

#==============================================================================

attr1 = ['上海','广东','北京','浙江','湖北','四川','重庆','江苏','陕西','湖南','安徽','福建','江西','河南','天津']
value1 = [613,924,196,131,95,93,31,134,61,34,30,22,17,15,9]

map = Map("2019统计学数据分析岗位招聘分布", width=1200, height=600,title_pos="center")
map.add(
    "",
    attr1,
    value1,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
    is_label_show=True
)
map.render(r'D:\BI大屏\统计学招聘报告\2019招聘分布地图.html')