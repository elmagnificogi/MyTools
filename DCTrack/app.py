from flask import Flask, jsonify
import requests
import time
import threading
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
d2api = "https://diablo2.io/dclone_api.php"
dcTrackInfo, dcTrackTimeStamp, user_count = "", time.time(), 0
lock = threading.Lock()



def getDCInfo():
    global dcTrackTimeStamp, dcTrackInfo
    try:
        dcTrackTimeStamp = time.time()
        print(dcTrackTimeStamp)
        dcTrackInfo = requests.get(d2api, timeout=10).json()
    except:
        pass


@app.route('/', methods=['GET'])
def dctrackinfo():
    try:
        if lock.acquire(blocking=False):
            global dcTrackTimeStamp, dcTrackInfo, user_count
            user_count += 1
            if time.time() - dcTrackTimeStamp > 5:
                print("user count: {}".format(user_count))
                user_count = 0
                getDCInfo()
            lock.release()
    except:
        lock.release()
    return jsonify(dcTrackInfo)

@app.route('/test', methods=['GET'])
def test():
    global dcTrackTimeStamp, dcTrackInfo, user_count
    user_count += 1
    #try:
        #if lock.acquire(blocking=False):
    # if time.time() - dcTrackTimeStamp > 5:
    #     print("user count: {}".format(user_count))
    #     user_count = 0
    #     getDCInfo()
            #lock.release()
    #except:
    #    lock.release()
    print("test:"+str(user_count))
    return "test:"+str(user_count)

@app.route('/t', methods=['GET'])
def t():
    global dcTrackTimeStamp, dcTrackInfo, user_count
    user_count += 1
    try:
        if lock.acquire(blocking=False):
            if time.time() - dcTrackTimeStamp > 5:
                print("user count: {}".format(user_count))
                user_count = 0
                getDCInfo()
            lock.release()
    except:
       lock.release()
    return jsonify(dcTrackInfo)

getDCInfo()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
