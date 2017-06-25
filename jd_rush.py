# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:18:52 2017

@author: tedoreve
"""

from selenium import webdriver
import time
#==============================================================================
        
def download(url,post,t):
    
#    driver = webdriver.Chrome()
    driver = webdriver.Firefox()
#    driver = webdriver.Chrome()
    driver.get(url[0])
    time.sleep(5)
    driver.get(url[1])
    time.sleep(1)
    while True:
        try:
            a = driver.find_element_by_xpath('//div[@class="mod_container"]/div[@class="seckill_container"]\
            /div[@class="skwrap"]/div[@class="spsk"]/div[@class="grid_c1"]/ul[@class=\
            "seckill_mod_goodslist clearfix"]/div[@class="spsk_item seckill_mod_goods_soldout"]/\
            div[@class="spsk_item_container"]/div[@class="spsk_item_title"]/a[@class="spsk_item_btn"]').text
            if a != '更多优惠':
                driver.find_element_by_xpath('//div[@class="mod_container"]/div[@class="seckill_container"]\
                                             /div[@class="skwrap"]/div[@class="spsk"]/div[@class="grid_c1"]/ul[@class=\
                                             "seckill_mod_goodslist clearfix"]/div[@class="spsk_item seckill_mod_goods_soldout"]/\
                                             div[@class="spsk_item_container"]/div[@class="spsk_item_title"]/a[@class="spsk_item_btn"]').click()
                break
            print('again')
            
        except:
            print('error')
            continue

#==============================================================================
if __name__=='__main__':

    url  = ['https://passport.jd.com/new/login.aspx','https://miaosha.jd.com/']
                
    post = [' 201418002509026',' 19910805.']
    
    t    = 1
    
    a = download(url,post,t)

    