import os
import glob
import json
import time
import requests
import websocket
from config import stream_url, push_url, header


def welcome_message():
    print('CommandCentre - created by Charlie Cook\n')
    print('Load plugins by placing suitable .py files in the plugins folder.\n\n')


def exit_system():
    print('\nCommandCentre - Shutting down\n')
    exit()


hooks = {}
plugin_names = []

for file in glob.glob('plugins\*.py'):
    file_no_extension = (os.path.basename(os.path.splitext(file)[0]))
    if file_no_extension == '__init__':
        break
    else:
        plugin_names.append(file_no_extension)

for plugin in plugin_names:
    exec('from plugins import {!s}'.format(plugin))
    exec('hooks[{!s}.hook] = {!r}'.format(plugin, plugin))

run = True
welcome_message()

pushbullet_stream = websocket.create_connection(stream_url)

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
                    check_hook = received_command.split(' ', 1)[0]
                    command = received_command.split(' ', 1)[1:]
                    if check_hook in hooks.keys():
                        exec('{!s}.run_command({!r})'.format(hooks[check_hook], command))
                    elif check_hook == 'Exit':
                        exit_system()
    except KeyError:
        pass
    time.sleep(0.5)
