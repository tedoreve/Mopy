# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:08:15 2017

@author: tedoreve
"""

# -*- coding:utf8 -*-
#!/usr/bin/python
# Python:          2.7.8
# Platform:        Windows
# Authro:          wucl
# Program:         端口扫描
# History:         2015.6.1
 
import socket, time, _thread
socket.setdefaulttimeout(3)
 
def socket_port(ip,port):
    """
    输入IP和端口号，扫描判断端口是否开放
    """
    try:
        if port>=65535:
            print(u'端口扫描结束')
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        if result==0:
            lock.acquire()
            print(ip,u':',port,u'端口开放')
            lock.release()
        s.close()
    except:
        print(u'端口扫描异常')
 
def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    try:
        print(u'开始扫描 %s' % ip)
        start_time=time.time()
        for i in range(0,65534):
            _thread.start_new_thread(socket_port,(ip,int(i)))
        print(u'扫描端口完成，总共用时 ：%.2f' %(time.time()-start_time))
        input("Press Enter to Exit")
    except:
        print(u'扫描ip出错')
         
 
if __name__=='__main__':
    url=input('Input the ip you want to scan:\n')
    lock=_thread.allocate_lock()
    ip_scan(url)