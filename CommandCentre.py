import json
import time
import requests
import websocket
from sys import exit

from APIToken import token

stream_url = "wss://stream.pushbullet.com/websocket/" + token
push_url = "https://api.pushbullet.com/v2/pushes?limit=1"
header = {'Access-Token': token}
run = True

pushbullet_stream = websocket.create_connection(stream_url)

print("CommandCentre - created by Charlie Cook")

while run is True:
    result = pushbullet_stream.recv()
    try:
        parsed_json = json.loads(result)
        if parsed_json['subtype'] == 'push':
            latest_push = requests.get(push_url, headers=header)
            if latest_push.status_code == 200:
                push_json = json.loads(latest_push.text)
                if push_json['pushes'][0]['type'] == 'note':
                    print(push_json['pushes'][0]['body'])
                    if push_json['pushes'][0]['body'] == 'Exit':
                        exit()
    except KeyError:
        pass
    time.sleep(0.5)
