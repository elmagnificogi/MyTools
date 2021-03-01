#-*- coding: utf-8 -*-

#!/usr/bin/python

import paramiko
import yaml
import threading
import sys,os

def ssh2(ip,username,passwd,cmd):

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)

        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            # for some unknown reason cant get stdout
            #out = stdout.readlines()
            #屏幕输出
            #for o in out:
            #    print(o)

        print('%s\tOK\n'%(ip))
        ssh.close()

    except :
        print('%s\tError\n'%(ip))

if __name__=='__main__':
    cmd = []
    # 登录用户名称
    username = 'pi'
    # 登录密码
    passwd = 'raspberry'

    #a = ['172.16.1.'+str(x) for x in range(1,256)]
    #b = ['172.16.2.'+str(x) for x in range(1,256)]
    #c = ['172.16.3.'+str(x) for x in range(1,256)]
    d = ['172.16.4.'+str(x) for x in range(185,188)]
    #e = ['172.16.5.'+str(x) for x in range(1,256)]

    ip_table = d#a+b+c+d+e

    for ip in ip_table:
        ret=os.system('ping -n 1 -w 1 %s'%ip)
        if ret:
            # just jump it
            pass;
        else:
            # 本质上 使用的是 /s/xx/xxx/g 的替换命令
            # 开启信息流
            #cmd.append("sudo sed -in \"s/^#\/home/\/home/g\" /etc/rc.local")
            cmd.append("sudo /home/pi/mav/mmp.py --in=/dev/ttyAMA0,115200 --out=172.16.200.1:14550 --log=/home/pi/mav/mav.log &")

            cmd.append("\n")

            # 关闭信息流
            #cmd.append("sudo sed -in \"s/^\/home/#\/home/g\" /etc/rc.local")

            # 重启
            #cmd.append("sudo reboot");

            print ("Beging Exec:%s on server ip: %s..." % (cmd, ip))

            ssh2(ip, username, passwd, cmd)

            print ("Done!")
    a = input()


