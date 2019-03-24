#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created March 2019

@author: othornew
"""

import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf 


def arp_scan(interface, ips):

	print("[*] Scanning...") 
	start_time = datetime.now()

	conf.verb = 0 
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), 
		     timeout = 2, 
		     iface = interface,
		     inter = 0.1)

	print ("\n[*] IP - MAC") 
	for snd,rcv in ans: 
		print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))
	stop_time = datetime.now()
	total_time = stop_time - start_time 
	print("\n[*] Scan Complete. Duration:", total_time)

if __name__ == "__main__":
    arp_scan(sys.argv[1], sys.argv[2])
