# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
import time
import random

#==============================================================================
def explorer(browser):
    #定义driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.get('http://www.bilibili.com/html/help.html#p')
        driver.find_element_by_xpath('//a[@id="bilibiliHtml5GrayTestBtn"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[@id="html5graypanel"]/div[@style="font-size: 14px; color: #222; line-height: 24px;"]/label/input').click()
    else:
        driver = webdriver.Firefox()
    return driver
        
def play(urllist,timelist,mode,t,time0,browser):

    #不要动，我也不知道是啥
    firefoxProfile = webdriver.FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.stylesheet', 2)
    firefoxProfile.set_preference('permissions.default.image', 2)
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
    firefoxProfile.set_preference("http.response.timeout", 5)
    firefoxProfile.set_preference("dom.max_script_run_time", 5)

    #随机列表
    source = random.sample(range(len(urllist)), len(urllist))

    #设置初始值
    element      = '//div[@class="player"]'
    if not t:
        t            = 1
    if not time0:
        time0        = 5
    i            = int(t) - 1
    time0        = int(time0)
    timeofload   = time0*2
    timeofbuffer = time0
    timeofnext   = time0
    
    driver = explorer(browser)

    while True:
        index = i
        if mode == 's' or mode == 'shuffle':
            index = source[i]
        try:
            #防止网页缓冲过长
            driver.set_page_load_timeout(timeofload)
            driver.get(urllist[index])
            print()
            print('第'+str(index+1)+'个视频缓冲时间少于'+str(timeofload))
        except Exception:
            print()
            print('第'+str(index+1)+'个视频缓冲超时，吃药之后萌萌哒')
        try:
            #最大化浏览器,不想最大化的话就注释掉
            driver.maximize_window()
            #最大化播放器,不想最大化的话就注释掉
            driver.find_element_by_xpath\
            (element+'/div[@id="bilibiliPlayer"]/div[@class="bilibili-player-area video-state-pause"]/div[@class="bilibili-player-video-control"]/div[@name="browser_fullscreen"]').click()
            print()
            print('第'+str(index+1)+'个视频全屏成功')
            #防止命令太近反应不过来
            time.sleep(timeofbuffer)
            #播放
            driver.find_element_by_xpath(element).click()
            print()
            print('第'+str(index+1)+'个视频播放成功')

            #随时检测是否在播放，一旦关闭播放器就重新开一个
            try:
                for j in range(int(timelist[index]/timeofnext)):
                    driver.current_url
                    #视频持续时间
                    time.sleep(timeofnext)
            except:
                print()
                print('手动开始播放下一视频')
                driver = explorer(browser)

        except Exception:
            #如果有错误，先测试浏览器是否关闭，若关闭则打开一个新的，若没有关闭，加1指数，继续循环
            try:
                driver.current_url
            except:
                driver = explorer(browser)
            print()
            print('致命错误，吃药之后萌萌哒')
            i = i+1
            if i == len(urllist):
                i = 0
            continue
        #一切正常后加1指数循环
        i = i+1
        #防止指数溢出
        if i == len(urllist):
            i = 0

#==============================================================================
if __name__=='__main__':

    #视频网址
    urllist = [
            'http://www.bilibili.com/video/av8247204/',
            'http://www.bilibili.com/video/av3366603/',
            'http://www.bilibili.com/video/av1268718/',
            'http://www.bilibili.com/video/av5337457/',
            'http://www.bilibili.com/video/av6948843/',
            'http://www.bilibili.com/video/av78287/',
            'http://www.bilibili.com/video/av3816897/',
            'http://www.bilibili.com/video/av6283649/',
            'http://www.bilibili.com/video/av7598870/',
            'http://www.bilibili.com/video/av8269718/',
            'http://www.bilibili.com/video/av2541782/',
            'http://www.bilibili.com/video/av6845663/',
            'http://www.bilibili.com/video/av3818869/',
            'http://www.bilibili.com/video/av7467947/',
            'http://www.bilibili.com/video/av2565074/',
            'http://www.bilibili.com/video/av7479076/',
            'http://www.bilibili.com/video/av4404099/',
            'http://www.bilibili.com/video/av2648921/',
            'http://www.bilibili.com/video/av2069286/',
            'http://www.bilibili.com/video/av2098846/',
            'http://www.bilibili.com/video/av2440804/',
            'http://www.bilibili.com/video/av1252354/',
            'http://www.bilibili.com/video/av1445995/',
            'http://www.bilibili.com/video/av1827504/',
            'http://www.bilibili.com/video/av1541797/',
            'http://www.bilibili.com/video/av1528441/',
            'http://www.bilibili.com/video/av1066202/',
            'http://www.bilibili.com/video/av8235658/',
            'http://www.bilibili.com/video/av5700746/',
            'http://www.bilibili.com/video/av2537319/',
            'http://www.bilibili.com/video/av345660/',
            'http://www.bilibili.com/video/av7029/',
            'http://www.bilibili.com/video/av3327562/',
            'http://www.bilibili.com/video/av6080584/',
            'http://www.bilibili.com/video/av5176035/',
            'http://www.bilibili.com/video/av7439521/',
            'http://www.bilibili.com/video/av4283472',
            'http://www.bilibili.com/video/av4465112/',
            'http://www.bilibili.com/video/av570885/',
            'http://www.bilibili.com/video/av2497369/',
            'http://www.bilibili.com/video/av8805389/',
            'http://www.bilibili.com/video/av5078483/',
            'http://www.bilibili.com/video/av7234117/',
            'http://www.bilibili.com/video/av1844227/',
            'http://www.bilibili.com/video/av7732290/',
            'http://www.bilibili.com/video/av3911005/',
            'http://www.bilibili.com/video/av1987195',
            'http://www.bilibili.com/video/av3905466/',
            'http://www.bilibili.com/video/av8709991/',
            'http://www.bilibili.com/video/av4492594/',
            'http://www.bilibili.com/video/av5023588/',
            'http://www.bilibili.com/video/av8390254/',
            'http://www.bilibili.com/video/av5658553/'
            ]

    #视频持续播放时间，与网址相对应（单位 秒）
    timelist = [
            58,
            110,
            150,
            185,
            237,
            45,
            246,
            246,
            181,
            87,
            188,
            153,
            163,
            272,
            284,
            191,
            275,
            186,
            291,
            316,
            207,
            274,
            245,
            196,
            132,
            89,
            222,
            290,
            147,
            206,
            282,
            214,
            219,
            48,
            202,
            112,
            240,
            151,
            217,
            214,
            199,
            218,
            297,
            176,
            268,
            238,
            244,
            202,
            258,
            264,
            160,
            112,
            230
            ]
    input('B站播放列表小程序bililist,源码https://github.com/tedoreve/. 按回车继续：')
    mode          = input('(默认循环,输入r代表循环播放,输入s代表随机播放)  请输入参数设定播放模式: ')
    index         = input('(默认第一个,播放列表不能为空,随机的话就无效了)  请设定从第几个视频开始播放：')
    timeofbuffer  = input('(默认5,推荐3~7,网络慢就用大一些的值)           请设定缓冲时间：')
    browser       = input('(默认firefox),输入chrome或者firefox           请设定浏览器:')
    play(urllist,timelist,mode,index,timeofbuffer,browser)
