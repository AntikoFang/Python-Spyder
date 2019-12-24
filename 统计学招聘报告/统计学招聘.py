# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:38:08 2019

@author: AntikoFang
@IDE：spyder
内容：爬取前程无忧招聘网站上搜索统计学关键词的招聘信息
"""
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# 配置环境
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

chrome_options.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(
        executable_path=r'E:\chromedriver\chromedriver.exe',
        options = chrome_options
        )


driver.get('https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25BB%259F%25E8%25AE%25A1%25E5%25AD%25A6,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')


#职位名称
name = []
#薪资
salary = []
#地址
place = []
# 学历
study = []
#福利
fine = []
#职位信息
info = []
# 职位类别
sort = []
for i in range(276):
    # 滚动屏幕
    driver.execute_script('window.scrollBy(0,1500)')
    # 提取职位文本
    HrefLists = driver.find_elements_by_xpath('//p[@class="t1 "]')
    # 去重
    hreftexts = set([Hrefs.text for Hrefs in HrefLists])
    for href in hreftexts:
        # 滚动屏幕
        driver.execute_script('window.scrollBy(0,30)')
        time.sleep(3)
        # 通过文本找到所有链接并点击
        driver.find_element_by_link_text(href).click()
        # pages = driver.find_element_by_link_text(href)
        # driver.execute_script("arguments[0].click();", pages)
        
        # 转到新打开的窗口
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])  
        
        # 职位名称
            #driver.find_element_by_xpath('//h1').text
        name.append(driver.find_element_by_xpath('//div[@class="cn"]/h1').text)
        # 薪资
        salary.append(driver.find_element_by_xpath('//div[@class="cn"]/strong').text)
        # 地址
        place.append(driver.find_element_by_xpath('//p[@class="msg ltype"]').text)
        # 学历
        study.append(driver.find_element_by_xpath('//p[@class="msg ltype"]').text)
        # 福利
        fine.append(driver.find_element_by_xpath('//div[@class="t1"]').text)
        #职位信息
        info.append(driver.find_element_by_xpath('//div[@class="tBorderTop_box"]').text)
        # 职位类别
        sort.append(driver.find_element_by_xpath('//a[@class="el tdn"]').text)
        
        driver.close()
        # 回到开始页面
        driver.switch_to.window(windows[0])
        time.sleep(2)
        
    # 点击下一页
    driver.find_element_by_partial_link_text('下一页').click()
    
# 汇总
df = pd.DataFrame([name,salary,place,study,fine,info,sort],
                  index = ['名称','薪资','地点','学历','好处','职位信息','类别'],
                  columns = name)
df.to_excel(r'C:\Users\Administrator\Desktop\统计学招聘信息.xlsx')

