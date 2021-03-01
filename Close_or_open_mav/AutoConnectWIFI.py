#-*- coding: utf-8 -*-

#!/usr/bin/python

import paramiko
import sys,os

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
            print(ip)
            tran  = paramiko.Transport((ip,22))
            tran.connect(username='pi',password=passwd)
            sftp = paramiko.SFTPClient.from_transport(tran)
            #将test.py 上传至 /tmp/test_new.py
            sftp.put('./autowifi.py','/home/pi/autowifi.py')

            # 增加文件权限
            cmd.append("sudo chmod 755 /home/pi/autowifi.py")

            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip,22,username,passwd,timeout=5)

                ssh.exec_command("sudo chmod 755 /home/pi/autowifi.py")
                stdin, stdout, stderr = ssh.exec_command("grep 'auto' -rn /home/pi/autowifi.py")

                out = stdout.readlines()
                if len(out)<1:
                    ssh.exec_command("sudo sed -in '/^\/home/a\\/home/pi/autowifi.py &' /etc/rc.local")
                    ssh.exec_command("sudo /home/pi/autowifi.py")

                print('%s\tOK\n'%(ip))
                ssh.close()

            except :
                print('%s\tError\n'%(ip))

            print ("Done!")
    a = input()


