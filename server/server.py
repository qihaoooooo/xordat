import json
import re
import requests
from flask import Flask, request
import command

#
#   API
#

class Message():

    data = {}

    def __init__(self, chat_id, reply_id=None):
        self.data["chat_id"] = chat_id
        if reply_id is not None:
            self.data["reply_to_message_id"] = reply_id

    def set_text(self, text):
        self.data["text"] = text

    def send(self):
        requests.post(get_url("sendMessage"), data=self.data)

# returns a URL for methods from the Telegram API
def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(tokens["telegram-bot-key"], method)

#
#   Logic
#

# regex patterns
item_regex = re.compile(r"((?<=\[)[a-zA-Z]+(?: [a-zA-Z]+)*(?=\]))+")

def handle_message(update):

    message = update["message"]

    if "text" in message:

        print("Received message")

        # identifier for message
        message_id = message["message_id"]
        # message text
        text = message["text"]
        # identifier for chat group message was sent in
        chat_id = message["chat"]["id"]

        # Message object for bot response
        response = Message(chat_id, message_id)

        # identifies commands
        if text[0] == "/" and len(text) > 1:

            print("Identified command: {}".format(text))

            # split into command name and params (if any)
            cmdlist = text[1:].split(" ")
            cmdname = cmdlist[0].split("@")

            # parse command only if directed at padordis or broadcast to all bots
            if len(cmdname) == 1 or (len(cmdname) == 2 and cmdname[1] == "padordis"):
                command.parse(cmdlist, response)

        # identifies item queries
        elif item_regex.search(text):

            item_list = item_regex.findall(text)

            # temporary code just for echoing
            for item in item_list:
                response.set_text(item)
                response.send()

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
