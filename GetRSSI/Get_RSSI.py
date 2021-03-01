#-*- coding: utf-8 -*-

#!/usr/bin/python 

import paramiko
import yaml
import threading
import msvcrt
import re

if __name__=='__main__':
    print ("加载，准备测量\n")
    f = open("settings.yaml",'r',encoding='UTF-8')
    config = yaml.load(f)
    f.close()

    # 需要执行的命令
    #cmd = config['execs']
    cmd = []
    # 登录用户名称
    username = config['username']
    # 登录密码
    passwd = config['passwd']

    # 登录IP列表
    ips = config['ips']

    threads = []
    ssh = []

    # connect
    for i in range(0, len(ips)):
        ip = "192.168.1." + str(100+ips[i]);

        try:
            ssh.append(paramiko.SSHClient())

            ssh[i].set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh[i].connect(ip,22,username,passwd,timeout=5)




        except:
            print("%s\tError\n" % (ip))

    # open data out file
    fout = open("RSSI.csv","w+")

    a = 'a'
    print ("开始测量\n")
    while( a != 'q'):
        for i in range(0, len(ips)):
            ip = "192.168.1." + str(100+ips[i]);

            # 需要执行的命令
            cmd = []

            cmd.append("sudo iw dev wlan0 link | grep -i --color signal");
            cmd.append("sudo iwconfig wlan0| grep -i --color Quality");

            print("Beging Exec:%s on server ip: %s...\n"%(cmd, ip))

            try:
                fout.write(ip)
                raw = []
                # first cmd 
                stdin, stdout, stderr = ssh[i].exec_command(cmd[0])
                out = str(stdout.readlines())
                out = out[4:-4]
                out = out.strip()
                raw = out.split(' ')
                #print(out)
                for o in raw:
                    fout.write(',' + o)

                # second cmd 
                stdin, stdout, stderr = ssh[i].exec_command(cmd[1])
                out = str(stdout.readlines())
                out = out[4:-4]
                out = out.strip()
                #print(out)
                raw = re.split('=| |/',out)
                #print(out)
                for o in raw:
                    fout.write(',' + o)

                # end
                fout.write("\n")

                print('%s\tOK\n' % (ip))
 
            except :
                print("%s\tError\n" % (ip))

        print ("Done!,输入回车继续，q键退出")
        a = input()
        #print(a)

    # close ssh
    for i in range(0, len(ips)):
        ssh[i].close()

    # close out file
    fout.close()

    print ("End!\n")
    a = input()


