from APIKey import token
# Config for Pushbullet

# URLS for Pushbullet service
stream_url = "wss://stream.pushbullet.com/websocket/" + token
push_url = "https://api.pushbullet.com/v2/pushes?limit=1"
header = {'Access-Token': token}