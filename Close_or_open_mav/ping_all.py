import threading,subprocess
from time import ctime,sleep,time
import queue
import os
import sys
import subprocess
import csv
import socket

queue=queue.Queue()
#print(sys.getdefaultencoding())
ping_data = dict()

class ThreadUrl(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):
        while True:
            host=self.queue.get()
            #ret=subprocess.call('ping -c 1 -w 1 '+host,shell=True,stdout=open('/dev/null','w'))
            ip = host
            #return1=os.system('ping -n 1 -w 1 %s'%ip)
            param = ['-n ','3 ','-w ','3 ',ip]
            p = subprocess.Popen(["ping.exe",param],
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                shell = True)
            out = p.stdout.read().decode("gb2312")
            #print(out)
            index = out.find("平均 = ")
            if index >= 4:
                print(ip+"-------平均延迟： "+out[index+5:-4].strip('\n').strip('\r')+'\n')
                ping_data[ip] = out[index+5:-4]
            self.queue.task_done()

def main():
    curpath = ""
    if getattr(sys, 'frozen', False):
        curpath = os.path.dirname(sys.executable)
    elif __file__:
        curpath = os.path.dirname(__file__)

    for i in range(100):
        t=ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    for host in ip_table:
        queue.put(host)
    queue.join()

    data = list()

    # get the table of ip,ping,id,ap
    for item in sorted(ping_data.keys(),key=socket.inet_aton):
        id = int(item.split('.')[2])*256+int(item.split('.')[3])
        data.append([item,ping_data[item],id,'dev_d5'+str(id)[0]])

    #print(data)

    # export the data into a csv file
    with open(curpath+'\ping.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    print('ping结果存放在:'+curpath+'ping.csv')
    print("总ping通数为：",len(data))


#网段要补全
a = []#['123.125.144.'+(str(x)).zfill(3) for x in range(1,254)] #ping 192.168.1 网段
b = ['192.168.1.'+(str(x)).zfill(0) for x in range(1,254)] #ping 192.168.1 网段
c = []

ip_table = a+b+c
start=time()
main()
print("耗时:%s",(time()-start))
input()
