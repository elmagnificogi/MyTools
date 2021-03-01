#-*- coding: utf-8 -*-

#!/usr/bin/python

import paramiko
import yaml
import threading

def ssh2(ip,username,passwd,cmd):

    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(ip,22,username,passwd,timeout=5)

        for m in cmd:

            stdin, stdout, stderr = ssh.exec_command(m)

#           stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            #屏幕输出

            for o in out:

                print(o)

        print('%s\tOK\n'%(ip))

        ssh.close()

    except :

        print('%s\tError\n'%(ip))





if __name__=='__main__':

    f = open("settings_ground_station.yaml",'r',encoding='UTF-8')
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

    # 更改前地面站ip地址最后一段
    ground_station = str(config['ground_station'])
    # 更改后地面站ip地址最后一段
    ground_station_new = str(config['ground_station_new'])

    threads = []

    for i in range(0, len(ips)):
        ip = "192.168.1." + str(ips[i]);

        # 需要执行的命令
        cmd = []
        # 本质上 使用的是 /s/xx/xxx/g 的替换命令
        cmd.append("sudo sed -in \"s/" + ground_station + ":14550/" + ground_station_new + ":14550/g\" /etc/rc.local")

        #cmd.append("sudo reboot");

        print ("Beging Exec:%s on server ip: %s..." % (cmd, ip))

        #a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
        #a.start()

        ssh2(ip, username, passwd, cmd)

    print ("Done!")
    a = input()


