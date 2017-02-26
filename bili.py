# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:49:51 2017

@author: tedoreve
"""

from selenium import webdriver
import time

#不要动，我也不知道是啥
firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
firefoxProfile.set_preference('permissions.default.image', 2)
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
firefoxProfile.set_preference("http.response.timeout", 5)
firefoxProfile.set_preference("dom.max_script_run_time", 5)

#定义driver
driver = webdriver.Firefox()

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
        'http://www.bilibili.com/video/av2497369/'
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
        214
        ]
#用来选择从第几个视频开始播放
t = 20

element='//div[@class="player"]'

while t < len(urllist):
    while True:
        try:
            driver.set_page_load_timeout(10)#防止网页缓冲过长
            driver.get(urllist[t])
            print('time'+str(t))
        except Exception:
            print('timeout'+str(t))
        try:
            #最大化浏览器,不想最大化的话就注释掉
            driver.maximize_window()
            #最大化播放器,不想最大化的话就注释掉
            driver.find_element_by_xpath\
            (element+'/div[@id="bilibiliPlayer"]/div[@class="bilibili-player-area video-state-pause"]/div[@class="bilibili-player-video-control"]/div[@name="browser_fullscreen"]').click()
            #防止命令太近反应不过来
            time.sleep(5)
                #播放
            driver.find_element_by_xpath(element).click()
            #视频持续时间
            time.sleep(timelist[t])
            t = t + 1
            #循环，不想循环的话就注释掉下面两行
            if t == len(urllist):
                t = 0
        except Exception:  
            print('Fatal Error')
            continue
        break
            

