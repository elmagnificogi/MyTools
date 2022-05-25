from flask import Flask, jsonify
import requests
import time
import threading
app = Flask(__name__)

class DCTrack:
    def __init__(self):
        self.d2api = "https://diablo2.io/dclone_api.php"
        self.dcTrackInfo, self.dcTrackTimeStamp, self.user_count = "", time.time(), 0
        self.lock = threading.Lock()
        
        
    def getDCInfo(self):
        global dcTrackTimeStamp, dcTrackInfo
        try:
            dcTrackTimeStamp = time.time()
            print(dcTrackTimeStamp)
            dcTrackInfo = requests.get(self.d2api, timeout=10).json()
        except:
            pass


    @app.route('/', methods=['GET'])
    def dctrackinfo(self):
        self.user_count+=1
        try:
            if self.lock.acquire(blocking=False):
                if time.time() - self.dcTrackInfo > 5:
                    print("user count: {}".format(self.user_count))
                    self.user_count = 0
                    self.getDCInfo()
                    self.lock.release()
        except:
            self.lock.release()
            return jsonify(self.dcTrackInfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
