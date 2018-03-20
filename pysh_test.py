#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import pyshark

pcap = pyshark.FileCapture(input_file="./captura1.pcap", keep_packets=True)

temp = x
x = y
y = temp    

# Hi nao160030! 

for p in pcap:
    p = str(p).replace('\n','')
    p_packet = re.match(r'.*Destination:\s+(?P<dstip>\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})\s+.*Source:\s+(?P<srcip>\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})\s+.*', p)
    if p_packet is not None:
        src_ip = p_packet.group('srcip')
        dst_ip = p_packet.group('dstip')
        print('SRC: {0:s} -> DST: {1:s}'.format(src_ip, dst_ip))
