import json
import re
import requests
from flask import Flask, request
import command

#
#   API
#

# returns a URL for methods from the Telegram API
def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(tokens["telegram-bot-key"], method)

# sends a message
def send_message(chat_id, text, reply_to_message_id=None):

    url = get_url("sendMessage")

    # build Message JSON object
    data = {}
    data["chat_id"] = chat_id
    data["text"] = text
    # checks if this is a reply to a message
    if reply_to_message_id is not None:
        data["reply_to_message_id"] = reply_to_message_id

    requests.post(url, data=data)

#
#   Logic
#

# regex patterns
item_regex = re.compile(r"((?<=\[)[a-zA-Z]+(?: [a-zA-Z]+)*(?=\]))+")
cmd_regex = re.compile(r"(?<=^/)([a-zA-Z_]*?)(?:@padordis)?$")

def handle_message(update):

    message = update["message"]

    if "text" not in message:
        # ignore non-text messages
        return

    # identifier for message
    message_id = message["message_id"]
    # message text
    text = message["text"]
    # identifier for chat group message was sent in
    chat_id = message["chat"]["id"]

    if cmd_regex.search(text):
        command.process(text)

    if item_regex.search(text):
        # message contains query of item(s)
        item_list = item_regex.findall(text)

        # temporary code just for echoing
        for item in item_list:
            send_message(chat_id=chat_id, text=item, reply_to_message_id=message_id)

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

    update = request.get_json()
    if "message" in update:
        # possibly a text message containing item query or command
        handle_message(update)

    return "OK"
