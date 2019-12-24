# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:25:07 2019

@author: AntikoFang
"""
# 今年薪资
#=============================================================================
import pandas as pd
excel = pd.read_excel(r'C:\Users\Administrator\Desktop\tongjixue1.xlsx')

a = []
a_avg = []
for i in range(0,len(excel["薪资"])):
    dw = excel["薪资"][i][-3:]
    a = excel["薪资"][i][0:-3].split("-")
    if dw == '千/月':
        a_avg.append((float(a[0])+float(a[1]))*500)
    elif dw == '万/月':
        a_avg.append((float(a[0])+float(a[1]))*5000)
    elif dw == '万/年':
        a_avg.append((float(a[0])+float(a[1]))*5000/12)
        
#excel["平均薪资"] = a_avg
#excel.to_excel(r'C:\Users\Administrator\Desktop\tongjixue1.xlsx')

b0 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0

for avg in a_avg:
    if avg <= 10000:
        b0 += 1
    elif avg <= 20000:
        b1 += 1
    elif avg <= 30000:
        b2 += 1    
    elif avg <= 40000:
        b3 += 1
    elif avg <= 50000:
        b4 += 1
    elif avg <= 70000:
        b5 += 1      
    elif avg <= 90000:
        b6 += 1
    else:
        b7 += 1
b = [b0,b1,b2,b3,b4,b5,b6,b7]
# 去年薪资
#=============================================================================
excel1 = pd.read_excel(r'C:\Users\Administrator\Desktop\tongjixue1.xlsx',sheet_name = 1)
excel2 = pd.read_excel(r'C:\Users\Administrator\Desktop\tongjixue1.xlsx',sheet_name = 2)

a1_avg = []
for i in range(0,len(excel1["薪资区间"])):
    a1 = excel1["薪资区间"][i].replace("k","000").split("-")
    a1_avg.append(float(a1[0])+float(a1[1]))
     
for j in range(0,len(excel2["薪资"])):
    dw1 = excel["薪资"][j][-3:]
    a1 = excel["薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a1_avg.append((float(a[0])+float(a[1]))*500)
    elif dw1 == '万/月':
        a1_avg.append((float(a[0])+float(a[1]))*5000)
    elif dw1 == '万/年':
        a1_avg.append((float(a[0])+float(a[1]))*5000/12)
        
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
for avg1 in a1_avg:
    if avg1 <= 10000:
        c0 += 1
    elif avg1 <= 20000:
        c1 += 1
    elif avg1 <= 30000:
        c2 += 1    
    elif avg1 <= 40000:
        c3 += 1
    elif avg1 <= 50000:
        c4 += 1
    elif avg1 <= 70000:
        c5 += 1      
    elif avg1 <= 90000:
        c6 += 1
    else:
        c7 += 1
c = [c0,c1,c2,c3,c4,c5,c6,c7]
attr = ['0-1万','1-2万','2-3万','3-4万','4-5万','5-7万','7-9万','大于9万']

from pyecharts import Bar
bar = Bar('2018-2019薪资对比柱状图')
#bar.use_theme("dark")  
bar.add('2019',attr,b,mark_point=['average'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross')  #追加最大值标记点、最小值标记点 
bar.add('2018',attr,c,mark_point = ['average'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross',bar_category_gap=45)  #追加最大值标记点、最小值标记点 
bar.render(r"D:\BI大屏\图\薪资对比柱状图.html")


# 专业薪资
#=============================================================================
import pandas as pd
excel1 = pd.read_excel(r'C:\Users\Administrator\Desktop\tongjixue.xlsx',sheet_name = 4)

a_avg = []
for j in range(0,len(excel1["算法工程师"])):
    dw1 = excel1["excel薪资"][j][-3:]
    a = excel1["excel薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a_avg.append((float(a[0])+float(a[1]))*500)
    elif dw1 == '万/月':
        a_avg.append((float(a[0])+float(a[1]))*5000)
    elif dw1 == '万/年':
        a_avg.append((float(a[0])+float(a[1]))*5000/12)       
sum(a_avg)/len(a_avg)

a1_avg = []
for j in range(0,len(excel1["数据分析员薪资"])):
    dw1 = excel1["数据分析员薪资"][j][-3:]
    a1 = excel1["数据分析员薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a1_avg.append((float(a1[0])+float(a1[1]))*500)
    elif dw1 == '万/月':
        a1_avg.append((float(a1[0])+float(a1[1]))*5000)
    elif dw1 == '万/年':
        a1_avg.append((float(a1[0])+float(a1[1]))*5000/12)

a2_avg = []
for j in range(0,len(excel1["统计员薪资"])):
    dw1 = excel1["统计员薪资"][j][-3:]
    a2 = excel1["统计员薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a2_avg.append((float(a2[0])+float(a2[1]))*500)
    elif dw1 == '万/月':
        a2_avg.append((float(a2[0])+float(a2[1]))*5000)
    elif dw1 == '万/年':
        a2_avg.append((float(a2[0])+float(a2[1]))*5000/12)
        
a3_avg = []
for j in range(0,len(excel1["软件工程师薪资"])):
    dw1 = excel1["软件工程师薪资"][j][-3:]
    a3 = excel1["软件工程师薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a3_avg.append((float(a3[0])+float(a3[1]))*500)
    elif dw1 == '万/月':
        a3_avg.append((float(a3[0])+float(a3[1]))*5000)
    elif dw1 == '万/年':
        a3_avg.append((float(a3[0])+float(a3[1]))*5000/12)
        
a4_avg = []
for j in range(0,len(excel1["管理薪资"])):
    dw1 = excel1["管理薪资"][j][-3:]
    a4 = excel1["管理薪资"][j][0:-3].split("-")
    if dw1 == '千/月':
        a4_avg.append((float(a4[0])+float(a4[1]))*500)
    elif dw1 == '万/月':
        a4_avg.append((float(a4[0])+float(a4[1]))*5000)
    elif dw1 == '万/年':
        a4_avg.append((float(a4[0])+float(a4[1]))*5000/12)

def avg(a_avg):
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    for avg1 in a_avg:
        if avg1 <= 10000:
            c0 += 1
        elif avg1 <= 20000:
            c1 += 1
        elif avg1 <= 30000:
            c2 += 1    
        elif avg1 <= 40000:
            c3 += 1
        elif avg1 <= 50000:
            c4 += 1
        elif avg1 <= 70000:
            c5 += 1      
        elif avg1 <= 90000:
            c6 += 1
        else:
            c7 += 1
    c = [c0,c1,c2,c3,c4,c5,c6,c7]
    return c

attr = ['0-1万','1-2万','2-3万','3-4万']
a_list = avg(a_avg)[:-4]
a1_list = avg(a1_avg)[:-4]
a2_list = avg(a2_avg)[:-4]
a3_list = avg(a3_avg)[:-4]
a4_list = avg(a4_avg)[:-4]

from pyecharts import Bar
bar = Bar()
#bar.use_theme("dark")  
bar.add('算法工程师',attr,a_list,mark_point=['max'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross')  #追加最大值标记点、最小值标记点 
bar.add('数据分析员',attr,a1_list,mark_point = ['max'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross',bar_category_gap=45)  #追加最大值标记点、最小值标记点 
bar.add('统计员',attr,a2_list,mark_point = ['max'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross',bar_category_gap=45)  #追加最大值标记点、最小值标记点 
bar.add('软件工程师',attr,a3_list,mark_point = ['max'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross',bar_category_gap=45)  #追加最大值标记点、最小值标记点 
bar.add('管理',attr,a4_list,mark_point = ['max'],tooltip_trigger = 'axis',tooltip_axispointer_type = 'cross',bar_category_gap=45,is_label_show=True)  #追加最大值标记点、最小值标记点 

bar.render(r"D:\BI大屏\统计学招聘\前五职位薪资对比柱状图.html")


# 用pyechart 1.5.11版的命令
#==============================================================================
import pyecharts.charts as pyec
import pyecharts.options as opts

bar = pyec.Bar()
# 添加标题
bar.set_global_opts(title_opts = opts.TitleOpts(title = '2018-2019薪资比较图'))
bar.add_xaxis(attr)
bar.add_yaxis('2019',b)
bar.add_yaxis('2018',c)
bar.render(r"D:\BI大屏\图\薪资对比柱状图.html")

