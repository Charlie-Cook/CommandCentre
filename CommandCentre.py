import json
import websocket

from APIToken import token

stream_url = "wss://stream.pushbullet.com/websocket/" + token


def received_message(ws, message):
    parsed_json = json.loads(message)
    if parsed_json['subtype'] == 'push':
        print("Received a push")

pushbullet_stream = websocket.WebSocketApp(stream_url, on_message=received_message)

pushbullet_stream.run_forever()
