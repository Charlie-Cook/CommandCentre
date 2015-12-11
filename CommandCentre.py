import json
import time
import requests
import websocket
import subprocess
from APIToken import token

stream_url = "wss://stream.pushbullet.com/websocket/" + token
push_url = "https://api.pushbullet.com/v2/pushes?limit=1"
header = {'Access-Token': token}
run = True

pushbullet_stream = websocket.create_connection(stream_url)

print("CommandCentre - created by Charlie Cook")


def run_command(passed_cmd):
    if passed_cmd == "Vagrant up":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\Digital4357\\Documents\\PowershellScripts\\VagrantCommands -command up'])
        p.communicate()
    elif passed_cmd == "Vagrant halt":
        p = subprocess.Popen(['powershell.exe',
                              'C:\\Users\\Digital4357\\Documents\\PowershellScripts\\VagrantCommands -command halt'])
        p.communicate()


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
