# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:33:29 2015

@author: tedoreve
"""

import urllib.request
import time
s=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'\
,'t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-')
for i in s[5:]:
    for j in s:
        for k in s:
            req = urllib.request.urlopen(                                     \
            'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='+i+j+k+'.com')
            p=req.read().decode()
            print(i,j,k)
            time.sleep(1)
            if p[107]==0: #0为可用，1为不可用
                f = open('test.txt', 'w')
                f.write(p)               
                f.close()
            if i=='-' and j=='-' and k=='-':
                break