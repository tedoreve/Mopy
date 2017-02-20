# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 09:07:22 2017

@author: tedoreve
"""

from scapy.all import srp, Ether, ARP  
conf.sniff_promisc=False
IpScan = '192.168.114.1/24'  
try:  
    ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)  
except Exception as e:  
    print(e)  
else:  
    for send, rcv in ans:  
        ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")  
        print(ListMACAddr)  