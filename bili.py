# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
import time
from sys import argv
import random

#==============================================================================
def play(index,urllist,timelist,mode,timeofload,timeofbuffer):
    
    element='//div[@class="player"]'
    
    #不要动，我也不知道是啥
    firefoxProfile = webdriver.FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.stylesheet', 2)
    firefoxProfile.set_preference('permissions.default.image', 2)
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
    firefoxProfile.set_preference("http.response.timeout", 5)
    firefoxProfile.set_preference("dom.max_script_run_time", 5)
    
    #定义driver
    driver = webdriver.Firefox()
    
    source = random.sample(range(len(urllist)), len(urllist))
    i      = 0
    while True:
        index = i
        if mode == 2:
            index = source[i]
        try:
            driver.set_page_load_timeout(timeofload)#防止网页缓冲过长
            driver.get(urllist[index])
            print('time'+str(index))
        except Exception:
            print('timeout'+str(index))
        try:
            #最大化浏览器,不想最大化的话就注释掉
            driver.maximize_window()
            #最大化播放器,不想最大化的话就注释掉
            driver.find_element_by_xpath\
            (element+'/div[@id="bilibiliPlayer"]/div[@class="bilibili-player-area video-state-pause"]/div[@class="bilibili-player-video-control"]/div[@name="browser_fullscreen"]').click()
            #防止命令太近反应不过来
            time.sleep(timeofbuffer)
            #播放
            driver.find_element_by_xpath(element).click()
            #视频持续时间
            time.sleep(timelist[index])
        except Exception:  
            print('Fatal Error')
            continue
        i = i+1
        if i == len(urllist):
            i = 0

#==============================================================================
if __name__=='__main__':   
    #调用参数
    if len(argv) == 1:
        mode = 1
    elif argv[1] == '-r' or argv[1] == '-repeat' or argv[1] == '':
        mode = 1
    elif argv[1] == '-s' or argv[1] == '-shuffle':
        mode = 2
    else:
        print('请输入参数设定播放模式，比如"python bili.py -s": \n \
        -r和-repeat或者不输入参数都代表循环播放\n \
        -s和-shuffle都代表随机播放')
    
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
    
    index        = 45  #用来选择从第几个视频开始播放
    timeofload   = 10  #防止网页加载时间过长，网速慢就要调大，推荐5-20
    timeofbuffer = 5   #防止跳转下一视频太快，反应不过来，网速慢就要调大，推荐1-5
    play(index,urllist,timelist,mode,timeofload,timeofbuffer)
