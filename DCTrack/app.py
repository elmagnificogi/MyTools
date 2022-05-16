from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)
d2api = "https://diablo2.io/dclone_api.php"
server_socket = ""
dcTrackInfo = ""

user_count = 0
last_user_count = 0


def getDCInfo():
    global dcTrackInfo
    try:
        call = requests.get(d2api, timeout=10).json()
        dcTrackInfo = call
    except:
        dcTrackInfo = ""


def DCTrackLoop():
    global last_user_count
    global user_count
    while True:
        try:
            getDCInfo()
        except:
            pass
        time.sleep(5)
        last_user_count = user_count
        user_count = 0


@app.route('/', methods=['GET'])
def dctrackinfo():
    global user_count
    user_count += 1
    return jsonify(dcTrackInfo)


@app.route('/s', methods=['GET'])
def statistics():
    global last_user_count
    return "user count:" + str(last_user_count)

# start tracker
getDCInfo()
dctrack = threading.Thread(target=DCTrackLoop)
dctrack.start()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
