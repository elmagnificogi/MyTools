# coding=utf-8
import pymysql
import httplib2
from urllib.parse import urlencode  # python3


# 这个是用来统计当前数据库中房间ip的归属，主要用来分区用的

def ip_find(ip):
    params = urlencode({'ip': ip, 'datatype': 'jsonp', 'callback': ''})
    url = 'https://api.ip138.com/ip/?' + params
    headers = {"token": "你的token"}  # token为示例
    http = httplib2.Http()
    response, content = http.request(url, 'GET', headers=headers)
    result = eval(content.decode("utf-8"))
    print(content.decode("utf-8"))
    if result["ret"] == "ok":
        return result["data"]
    # find({"ret":"ok","ip":"34.101.155.80","data":["印度尼西亚","雅加达","","","谷歌云","","0062"]})
    #                                                  国家        省    市  区 运营商 邮政编码 地区区号


if __name__ == '__main__':
    db = pymysql.connect(host="服务器地址", user="root", password="密码", database="kdc_test")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # f_ip = open("./ip.txt",'r+')
    # ip_set = set()
    # lines = f_ip.readlines()
    # for line in lines:
    #     ip_set = ip_set | set([line])
    # 
    # print(ip_set)

    sql = "SELECT distinct ip FROM kdc_test.room"
    cursor.execute(sql)
    result = cursor.fetchall()
    # update all ip with their location and isp
    for r in result:
        print(r[0])
        sql = "select * from kdc_test.ip_statistics where ip=\"" + r[0] + "\""
        # print(sql)
        find = cursor.execute(sql)
        # print(find)
        if find == 0:
            data = ip_find(r[0])
            if data != None:
                sql = "insert into kdc_test.ip_statistics (`ip`, `country`, `province`, `isp`) values(\"" + r[
                    0] + "\",\"" + data[0] + "\",\"" + data[1] + "\",\"" + data[4] + "\")"
                # sql = "update kdc_test.ip_statistics set country =\""+data[0]+"\" and set province =\""+data[1]+"\" and set isp =\""+data[4]+"\" where ip=\""+r[0]+"\""
                print(sql)
                ret = cursor.execute(sql)
                db.commit()
            else:
                print("error:" + r[0])
        else:
            continue
            
    db.close()
