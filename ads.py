# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:23:25 2018

@author: tedoreve
"""

from selenium import webdriver
import time
import xlsxwriter

#==============================================================================
def init(browser):
    #定义driver
    if browser == 'chrome':

#        Options = webdriver.ChromeOptions()
#        Options.add_argument("--disable-bundled-ppapi-flash")
        driver = webdriver.Chrome()


    else:
#        Profile = webdriver.FirefoxProfile()
#        Profile.set_preference('permissions.default.stylesheet', 2)
#        Profile.set_preference('permissions.default.image', 2)
#        Profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
#        Profile.set_preference("http.response.timeout", 5)
#        Profile.set_preference("dom.max_script_run_time", 5)
        driver = webdriver.Firefox()
    return driver

def crawl(adslist,browser,time0,year):

    op  = 'http://adsabs.harvard.edu/cgi-bin/nph-ref_query?bibcode='
    ed  = '&amp;refs=CITATIONS&amp;db_key=AST'
    
    citations = {}

    time0        = int(time0)
    timeofbuffer = time0

    #
    driver = init(browser)

    for link in adslist:
        cup = []
        if '&' in link:
            link = link.replace('&','%26')           
        driver.get(op+link+ed)   
        time.sleep(timeofbuffer)
        try:
            cite  = driver.find_element_by_xpath('//form/input').get_attribute('value')
            if year in cite:
                print()
                print('文章'+link+'有引用:')
                for i in cite.split(';'):                   
                    if year in i:
                        print(i)
                        cup.append(i)
                    citations[link] = cup
        except:
            pass
        
    return citations


#==============================================================================
if __name__=='__main__':

    #文章网址
    urlobject = open('adslist.txt','r')
    adslist   = urlobject.read().splitlines()
    urlobject.close()


    print()
    input('统计文章引用小程序,源码https://github.com/tedoreve/. 按回车继续：')

    browser       = input('(默认firefox,输入chrome或者firefox)             请设定浏览器:')
    
    timeofbuffer  = 3
    
    year = '2017'

    citations = crawl(adslist,browser,timeofbuffer,year)
    
    workbook = xlsxwriter.Workbook('citations.xlsx')
    worksheet = workbook.add_worksheet()
    
    row = 0
    col = 0
    for key in citations.keys():
        row += 1
        worksheet.write(row, col, key)
        for item in citations[key]:
            worksheet.write(row, col + 1, item)
            row += 1
        
    workbook.close()