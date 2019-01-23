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

# sets webhook to URL provided
def set_webhook(url):

    url = "{}/{}".format(url, tokens["telegram-bot-key"])

    r = requests.post(get_url("setWebhook"), data={"url": url})
    res = r.json()

    if res["ok"]:
        r = requests.get(get_url("getWebhookInfo"))
        res = r.json()
        print("Successfully set webhook to [{}]".format(res["result"]["url"]))
    else:
        print("Failed to set webhook:")
        pp(res)

# detaches webhook
def detach_webhook():

    r = requests.post(get_url("setWebhook"), data={"url": ""})
    res = r.json()

    if res["ok"]:
        print("Successfully detached webhook")
    else:
        print("Failed to detach webhook:")
        pp(res)

if len(sys.argv) < 2:
    print("Explicitly declare flag --detach to detach webhook")
elif len(sys.argv) == 2:
    arg = sys.argv[1]
    if arg == "--detach":
        detach_webhook()
    else:
        # take as URL
        set_webhook(arg)
else:
    print("Too many arguments")
