# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:31:30 2017

@author: tedoreve
"""


from selenium import webdriver
import time
#==============================================================================
        
def main(url,post,t):
    
#    driver = webdriver.Chrome()
#    driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(url[0])
    time.sleep(10)
    driver.get(url[1])
    time.sleep(1)
    while True:
        a = time.ctime()
        print(a)
        if a[11:19] == '21:59:00':
            while True:
                try:
                    time.sleep(0.1)
                    driver.find_element_by_xpath('//div[@class="main"]/div[@class="quan-h-wrap"]\
                    /div[@class="w"]/div[@class="quan-h-cate"]/div[@class="cate-cont"]/div[@class=\
                    "quan-item quan-item02 quan-type01 item-44586583"]/div[@class="q-type"]/\
                    div[@class="q-ops-box"]/div[@class="q-opbtns"]/a[@class="btn btn-def"]/\
                    span[@class="txt"]').click()
                    break
                except:
                    print('again')
                    continue

def cloth(url,post,t):
    #    driver = webdriver.Chrome()
#    driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(url[0])
    time.sleep(10)
    driver.get(url[2])
    time.sleep(1)
    while True:
        a = time.ctime()
        print(a)
        if a[11:19] == '10:00:00':
            while True:
                try:
                    driver.find_element_by_xpath('//div[@id="25355860"]/div[@class="d-layout-one d-w990 "]\
                    /div[@class="  userdefined-153704 "]/div[@class="mc"]/div[@class="j-module"]/div[@class=\
                    "userDefinedArea"]/section[@class="quan-1"]/a[@href="//coupon.jd.com/ilink/couponSendFront/send_index.action?key=cd5b21c57ccd4cb0b19a2b0c3402943f&roleId=7021161&to=sale.jd.com/act/a3x6w2dhqio.html&"]').click()
                    time.sleep(50)
                    break
                except:
                    print('again')
                    continue
    
    

#==============================================================================
if __name__=='__main__':

    url  = ['https://passport.jd.com/new/login.aspx','https://a.jd.com/','https://sale.jd.com/act/a3x6w2dhqio.html']
                
    post = [' 201418002509026',' 19910805.']
    
    t    = 1
    
#    main(url,post,t)
    cloth(url,post,t)
