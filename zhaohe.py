# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from PIL import Image
import time
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.select import Select
#import os  #改路径
#import sys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#==============================================================================
        
def download(url,post,t):
    
#    driver = webdriver.Chrome()
    driver = webdriver.Firefox()
#    driver = webdriver.Chrome()
    driver.get(url[0])
#    time.sleep(10)
#    driver.get(url[1])
#    print(driver.page_source)
#    time.sleep(1)
#    while True:
#        try:
    a = driver.find_element_by_xpath('//div[@class="b-page-body"]/div[@class="main-inner"]\
    /div[@class="viewbox report-scroll-module"]/div[@class="info"]/div[@class="v-title-info"]\
    /div[@class="v-title-line v-rank"]/span').text
    print(a)
            
#            break
#        except:
#            print('again')
#            continue
#    box = driver.find_element_by_id("username") #定位box
##    box.send_keys(Keys.TAB) #在box点击鼠标
###    box.send_keys(post[0])  #在box输入
###    box = driver.find_element_by_name("-c.eq") #定位下拉列表
###    Select(box).select_by_index(7) #选择下拉列表
###    driver.find_element_by_xpath('//div[@id="vcst"]/table/tbody/tr/td[@align="RIGHT"]/input').send_keys(Keys.ENTER)
###    box = driver.find_element_by_name("-out.max") #定位下拉列表
###    Select(box).select_by_index(11) #选择下拉列表
###    box = driver.find_element_by_name("-out.form") #定位下拉列表
###    Select(box).select_by_index(0) #选择下拉列表
#    box = driver.find_element_by_id("pwd_tip")
#    box.send_keys(Keys.TAB) #在box点击鼠标
#    box.send_keys(post[1])  #在box输入
#    ActionChains(driver).context_click(box).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform() 
#    driver2 = webdriver.Firefox()
#    driver2.get(post[2])
#    time.sleep(2)
#    driver.get_screenshot_as_file('captcha.png')
#    
#    
##    print(driver.page_source)
#    im = Image.open('captcha.png')
#    im.show()
#    cap = input('captcha:')
#    im.close()
#    box = driver.find_element_by_id("captcha")
#    box.send_keys(Keys.TAB)
#    box.send_keys(cap)
#    box.send_keys(Keys.ENTER)
#    
#    time.sleep(2)
#    driver.get_screenshot_as_file('captcha.png')
#    im = Image.open('captcha.png')
#    im.show()
#    cap = input('captcha:')
#    im.close()
##    driver.get()

#==============================================================================
if __name__=='__main__':

    url  = ['http://www.bilibili.com/video/av10729120/']
                
    post = [' 201418002509026',' 19910805.']
    
    t    = 1
    
    a = download(url,post,t)
