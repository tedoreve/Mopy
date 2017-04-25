# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time

#==============================================================================
        
def download(url,post,t):

#    driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    driver.get(url)    
#    print(driver.page_source)

    box = driver.find_element_by_name("Coord")
    box.send_keys(Keys.TAB)
    box.send_keys(post[0])
    box.send_keys(Keys.ENTER)

#==============================================================================
if __name__=='__main__':

    url  = 'http://simbad.u-strasbg.fr/simbad/sim-fcoo'
    
    post = ['20 54 05.689 +37 01 17.38','2']
    
    t    = 1
    
    download(url,post,t)
    