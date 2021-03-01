import paramiko
import yaml
import os

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print (o)
                
        print('%s\tOK\n' % (ip))
        ssh.close()
    except :
        print("%s\tError\n" % (ip))
        
f = open("settings.yaml",'r',encoding='UTF-8')
config = yaml.load(f)
f.close()

# 登录用户名称
username = config['username']

# 登录密码
passwd = config['passwd']

# wifi ssid和密码
ssid = config["ssid"]
psk = config["psk"]

# 修改后ip
address = config["address"]

# 登录IP列表
ips = config['ips']

if len(ips) != len(address):
    print("error,要修改的IP数目不对等")
    a = input()
    os._exit(0)

for i in range(0, len(ips)):
    ip = "192.168.1." + str(ips[i]);

    # 需要执行的命令
    cmd = []

    if ssid != None:
        tmp = "sudo sed -in \"/^wpa-ssid/c wpa-ssid " + ssid + " \" /etc/network/interfaces"
        cmd.append(tmp)
    else:
        print ("ssid empty")

    if psk != None:
        tmp = "sudo sed -in \"/^wpa-psk/c wpa-psk " + str(psk) + " \" /etc/network/interfaces"
        cmd.append(tmp)
    else:
        print ("psk empty")

    if address != None:
        tmp = "sudo sed -in \"/^address/c address 192.168.1." + str(address[i]) + " \" /etc/network/interfaces"
        cmd.append(tmp)
    else:
        print ("address empty")

    cmd.append("sudo reboot");

    print ("Beging Exec:%s on ip: %s...\n"%(cmd, ip))

    ssh2(ip, username, passwd, cmd)

print ("修改完成,按任意键退出")
a = input()


