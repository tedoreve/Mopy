# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

#==============================================================================
        
def download(url,post,t):

#    driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
    driver.get(url)    
#    print(driver.page_source)

    box = driver.find_element_by_name("email")
    box.send_keys(Keys.TAB)
    box.send_keys(post[0])
    box = driver.find_element_by_name("password")
    box.send_keys(Keys.TAB)
    box.send_keys(post[1])
    
#    driver2 = webdriver.Firefox()
#    driver2.get(post[2])
    time.sleep(2)
    driver.get_screenshot_as_file('captcha.png')
    
    
#    print(driver.page_source)
    im = Image.open('captcha.png')
    im.show()
    cap = input('captcha:')
    im.close()
    box = driver.find_element_by_id("captcha")
    box.send_keys(Keys.TAB)
    box.send_keys(cap)
    box.send_keys(Keys.ENTER)
    
    time.sleep(2)
    driver.get_screenshot_as_file('captcha.png')
    im = Image.open('captcha.png')
    im.show()
    cap = input('captcha:')
    im.close()
#    driver.get()


#==============================================================================
if __name__=='__main__':

    url  = 'http://bangumi.tv/login'
    
    post = ['wlzzs666@sina.com','19910805','http://bangumi.tv/signup/captcha']
    
    t    = 1
    
    download(url,post,t)
    