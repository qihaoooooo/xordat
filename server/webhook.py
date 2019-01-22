#
#   Script to update Telegram bot webhook
#
import sys
import json
import requests
from pprint import pprint as pp

with open("tokens.json") as tf:
    tokens = json.load(tf)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(tokens["telegram-bot-key"], method)

if len(sys.argv) < 2:
    print("No webhook URL supplied")
    exit()

url = "{}/{}".format(sys.argv[1], tokens["telegram-bot-key"])

requests.post(get_url("setWebhook"), data={"url": url})
r = requests.get(get_url("getWebhookInfo"))
pp(r.json())
