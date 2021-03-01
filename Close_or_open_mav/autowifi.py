#!/usr/bin/env python

import os, time,sys
import subprocess

f = open('/home/pi/network.log', "w", 1) #buffing in line
sys.stdout = f
sys.stderr = f

reconnect_count = 0
reconnect = 5

while True:
    p = subprocess.Popen('ping -c1 172.16.200.1',shell=True, stdout=subprocess.PIPE)
    result = p.stdout.read()
    #print result.strip()
    if result.find('Unreachable') != -1:
        reconnect_count+=1
        print('lose connect')
    else:
        reconnect_count = 0

    if reconnect_count >= reconnect:
        print('reset network')
        os.system('sudo /etc/init.d/networking restart')
        reconnect_count = 0
        time.sleep(10)
    time.sleep(4) #