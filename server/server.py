import json
import re
import requests
from pprint import pprint as pp
from flask import Flask, request

#
#   API
#

# returns a URL for methods from the Telegram API
def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(tokens["telegram-bot-key"], method)

# sends a message
def send_message(chat_id, text, reply_to_message_id=None):

    print("Sending message")

    url = get_url("sendMessage")

    # build Message JSON object
    data = {}
    data["chat_id"] = chat_id
    data["text"] = text
    # checks if this is a reply to a message
    if reply_to_message_id is not None:
        data["reply_to_message_id"] = reply_to_message_id

    r = requests.post(url, data=data)
    pp(r.json())
    pp(data)
#   Logic
#

# regex patterns
item_regex = re.compile(r"(\[[a-zA-Z]+(?: [a-zA-Z]+)*\])+")

def handle_message(update):

    print("Received message")

    # properties of update
    message = update["message"]
    chat_id = message["chat"]["id"]

    if "text" in message:
        text = message["text"]
    else:
        # ignore non-text messages
        return

    print(chat_id)
    print(text)

    if item_regex.search(text):
        # message contains query of item(s)
        item_list = item_regex.findall(text)

        test_str = ', '.join(item_list)
        send_message(chat_id, test_str)

#
#   Server
#

# load API tokens
with open("tokens.json") as tf:
    tokens = json.load(tf)

app = Flask(__name__)

# route for handling updates from Telegram API
@app.route("/{}".format(tokens["telegram-bot-key"]), methods=["POST"])
def handle_update():

    print("Received update")

    update = request.get_json()
    if "message" in update:
        # possibly a text message containing item query or command
        handle_message(update)

    return "OK"
