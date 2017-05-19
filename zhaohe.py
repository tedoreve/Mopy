# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from PIL import Image
#import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
#import os  #改路径
#import sys
#==============================================================================
        
def download(url,post,t):

#    driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
    driver.get(url)    
#    print(driver.page_source)
    
    box = driver.find_element_by_id("itarget") #定位box
    box.send_keys(Keys.TAB) #在box点击鼠标
    box.send_keys(post[0])  #在box输入
    box = driver.find_element_by_name("-c.eq") #定位下拉列表
    Select(box).select_by_index(7) #选择下拉列表
#    driver.find_element_by_xpath('//div[@id="vcst"]/table/tbody/tr/td[@align="RIGHT"]/input').send_keys(Keys.ENTER)
    box = driver.find_element_by_name("-out.max") #定位下拉列表
    Select(box).select_by_index(11) #选择下拉列表
    box = driver.find_element_by_name("-out.form") #定位下拉列表
    Select(box).select_by_index(0) #选择下拉列表
    driver.find_element_by_xpath('//div[@id="vcst"]/table/tbody/tr/td[@align="RIGHT"]/input').click()
    box = driver.find_element_by_id("itarget")
    ActionChains(driver).context_click(box).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform() 
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

    url  = 'http://vizier.u-strasbg.fr/cgi-bin/VizieR?-source=B/2mass'
    
    post = ['205.5 0.5']
    
    t    = 1
    
    download(url,post,t)
    