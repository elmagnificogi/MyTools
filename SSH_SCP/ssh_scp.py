#-*- coding: utf-8 -*-

#!/usr/bin/python

import paramiko
import yaml
import threading

def scp(ip, username, passwd, local, remote):

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)

        sftp = ssh.open_sftp()
        for i in range(0, len(local)):
            if local[i] is None:
                del_cmd = "sudo rm -rf " + remote[i]
                stdin, stdout, stderr = ssh.exec_command(del_cmd, get_pty=True)
                out = stdout.readlines()
                # 屏幕输出
                for o in out:
                    print(o)
            else:
                sftp.put(local[i], remote[i])
        ssh.exec_command("sudo reboot");
        ssh.close()

    except Exception as e:

        print('%s\tError\n'%(ip))
        print('repr(e):\t', repr(e))




if __name__=='__main__':

    f = open("settings_scp.yaml")
    config = yaml.load(f)
    f.close()

    cmd = []
    # 登录用户名称
    username = config['username']
    # 登录密码
    passwd = config['passwd']
    # 登录IP列表
    ips = config['ips']
    # 本地文件名
    local_file = config['local_file']
    # 远端文件名
    remote_file = config['remote_file']

    threads = []

    for i in range(0, len(ips)):
        ip = "192.168.1." + str(ips[i]);

        print("Beging on server ip: %s..." % (ip))

        #a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
        #a.start()

        scp(ip, username, passwd, local_file, remote_file)
    
    print("End!")
    a = input()



