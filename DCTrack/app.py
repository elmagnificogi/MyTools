from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)
d2api = "https://diablo2.io/dclone_api.php"
dcTrackInfo, dcTrackTimeStamp, user_count = "", time.time(), 0


def getDCInfo():
    global dcTrackTimeStamp, dcTrackInfo
    dcTrackTimeStamp = time.time()
    dcTrackInfo = requests.get(d2api).json()



@app.route('/', methods=['GET'])
def dctrackinfo():
    global dcTrackTimeStamp, dcTrackInfo, user_count
    user_count += 1
    if time.time() - dcTrackTimeStamp > 5:
        print("user count: {}".format(user_count))
        user_count = 0
        getDCInfo()
    return jsonify(dcTrackInfo)


getDCInfo()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
