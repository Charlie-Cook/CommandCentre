import os
import sys
import glob
import json
import time
import requests
import websocket
from config import token, stream_url, push_url, header


def welcome_message():
    print('CommandCentre - created by Charlie Cook\n')
    print('Load plugins by placing suitable .py files in the plugins folder.\n\n')

plugin_names = []

for file in glob.glob('plugins\*.py'):
    file_no_extension = (os.path.basename(os.path.splitext(file)[0]))
    if file_no_extension == '__init__':
        break
    else:
        plugin_names.append(file_no_extension)

print(plugin_names)

run = False
# welcome_message()

# pushbullet_stream = websocket.create_connection(stream_url)

while run is True:
    result = pushbullet_stream.recv()
    try:
        parsed_json = json.loads(result)
        if parsed_json['subtype'] == 'push':
            latest_push = requests.get(push_url, headers=header)
            if latest_push.status_code == 200:
                push_json = json.loads(latest_push.text)
                if push_json['pushes'][0]['type'] == 'note':
                    received_command = push_json['pushes'][0]['body']
                    print(received_command)
                    if received_command == 'Exit':
                        exit()
                    else:
                        run_command(received_command)
    except KeyError:
        pass
    time.sleep(0.5)
