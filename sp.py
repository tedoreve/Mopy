# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#==============================================================================
        
def download(url,post,t):

#    driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
#    driver.set_page_load_timeout(t)
    driver.get(url)    
#    print(driver.page_source)

    box = driver.find_element_by_name("Coord")
    box.send_keys(Keys.TAB)
    box.send_keys(post[0])
    box.send_keys(Keys.ENTER)
#    print()
#    print('第'+str(index+1)+'个视频全屏成功')
#    #防止命令太近反应不过来
#    time.sleep(timeofbuffer)
#    #播放
#    driver.find_element_by_xpath(element).click()
#    print()
#    print('第'+str(index+1)+'个视频播放成功')

    #随时检测是否在播放，一旦关闭播放器就重新开一个
#    try:
#        for j in range(int(int(timelist[index].strip())/timeofnext)):
#            driver.current_url
#            #视频持续时间
#            time.sleep(timeofnext)
    




#==============================================================================
if __name__=='__main__':

    url  = 'http://simbad.u-strasbg.fr/simbad/sim-fcoo'
    
    post = ['20 54 05.689 +37 01 17.38','2']
    
    t    = 1
    
    download(url,post,t)
    