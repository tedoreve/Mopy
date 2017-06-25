# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#==============================================================================
        
def download(url,post,t):
    
#    driver = webdriver.Chrome()
    driver = webdriver.Firefox()
#    driver = webdriver.PhantomJS()
    for i in range(7):
        j = i + 12
        for k in range(13):
            l = k + 3
            if l < 10:
                username = ' hyzx' + str(j) + '0' + str(l)
            else:
                username = ' hyzx' + str(j) + str(l)
            driver.get(url) 
            try:
                driver.find_element_by_id('toLogOut')
                a = 'logged'
                print(a)
                return 'break'
            except:
                a = 'loging'
                print(a)
                wait = WebDriverWait(driver, 10)
                user = wait.until(EC.visibility_of_element_located((By.ID, "username_tip")))
                user.send_keys(username)
                pwd = wait.until(EC.visibility_of_element_located((By.ID, "pwd_tip")))
                pwd.send_keys(username)
                driver.find_element_by_id('loginLink_div').click()

    return a

#==============================================================================
if __name__=='__main__':

    url  = 'http://210.77.16.21'
                
    post = [' 201418002509026',' 19910805.']
    
    t    = 1
    
    a = download(url,post,t)
