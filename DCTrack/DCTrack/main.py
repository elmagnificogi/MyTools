import datetime
import socket
import requests
import threading
import time

from multiprocessing import Process

d2api = "https://diablo2.io/dclone_api.php"
server_socket = ""
dcTrackInfo = ""

now = time.time()
user_count = 0

def getDCInfo():
    global dcTrackInfo
    call = requests.get(d2api).json()
    print(call)
    dcTrackInfo = call

def handle_client(client_socket):
    global user_count
    global now
    """
    处理客户端请求
    """
    request_data = client_socket.recv(1024)
    # print("request data:", request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = str(dcTrackInfo)
    response = response_start_line + response_headers + "\r\n" + response_body

    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))

    cur = time.time()
    user_count+=1
    if cur - now > 5:
        now = cur
        print("User Num:"+str(user_count))
        user_count = 0
    # 关闭客户端连接
    client_socket.close()
 
def socketInit():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(65530)


def DCTrackLoop():
    while True:
        try:
            getDCInfo()
        except:
            pass
        time.sleep(5)
    print("DCTrackLoop End")

if __name__ == "__main__":
    getDCInfo()

    dctrack = threading.Thread(target=DCTrackLoop)
    dctrack.start()

    socketInit()
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            #print("[%s, %s]用户连接上了" % client_address)
            handle_client_process = Process(target=handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()
        except:
            socketInit()
        #print("Restart a new socket")

    print("DCTrack End")
    server_socket.close()
