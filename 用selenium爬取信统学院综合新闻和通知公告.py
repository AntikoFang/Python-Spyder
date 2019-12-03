# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(
        executable_path=r'E:\chromedriver\chromedriver.exe',
        options = chrome_options
        )

driver.get('http://xgxy.hbue.edu.cn/')
#print(driver.page_source)
title = driver.title

# 综合新闻
texts = driver.find_elements_by_xpath('//span[@class="Article_Title"]')
# 找到链接文本
items = [item.text for item in texts]
# 图片链接
imgs = driver.find_elements_by_xpath('//div[@class="fields ex_fields"]/span[1]/a/img')

text_title = []
text_content = []
for item in items:
    # 通过文本找到所有链接并点击
    driver.find_element_by_partial_link_text(item).click()
    # 转到新打开的窗口
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])  
    # 标题
    text_title.append(driver.find_element_by_xpath('//h1[@class="arti_title"]').text)
    # 内容
    text_content.append(driver.find_element_by_xpath('//div[@class="wp_articlecontent"]').text)
    # 回到开始页面
    driver.switch_to.window(windows[0])
    time.sleep(2)

# 通知公告
texts = driver.find_elements_by_xpath('//div[@class="news_tit"]')
# 找到链接文本
items1 = [item.text for item in texts]

text_title1 = []
text_content1 = []
for item1 in items1:
    # 通过文本找到所有链接并点击
    driver.find_element_by_partial_link_text(item1).click()
    # 转到新打开的窗口
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])  
    # 标题
    text_title1.append(driver.find_element_by_xpath('//h1[@class="arti_title"]').text)
    # 内容
    text_content1.append(driver.find_element_by_xpath('//div[@class="wp_articlecontent"]').text)
    # 回到开始页面
    driver.switch_to.window(windows[0])
    time.sleep(2)

code = driver.find_element_by_xpath('//div[@class="foot"]').text[-10:-4]

df = pd.DataFrame([title,text_title,text_content,text_title1,text_content1,code],
                  index = ['网页标题','综合新闻标题','综合新闻内容','通知公告标题','通知公告内容','邮编'])


# 网页标题


#print(driver.find_element_by_xpath('//title/text()'))

#try:
#    element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.TAG_NAME,'title').text)
#    print(element)
#finally:
#    print(driver.find_element_by_id('content').text)
#    driver.close()
#    pass