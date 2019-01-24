import requests
import json
import time
import playsound

storedAlerts = []
json_data = open('touchme.json', encoding='utf8')
desiredRewards = json.load(json_data)

def calcExpiry(expiry):
    return time.ctime(int(expiry)/1000)

def audio(path):
    playsound.playsound(path, True)

def refresh():

    r = requests.get('http://content.warframe.com/dynamic/worldState.php')
    data = json.loads(r.text)
    alerts = data["Alerts"]

    for alert in alerts:
        info = alert.get('MissionInfo')
        reward = info.get('missionReward')

        item = reward.get('items', 'none')
        citem = reward.get('countedItems', 'none')

        if citem is not 'none':
            item = citem[0].get('ItemType',)

        if item is not 'none':
            str = desiredRewards.get(''.join(item), 'none')
            missionID = alert['_id'].get('$oid')

            if str is not 'none' and missionID not in storedAlerts:
                expiryTime = calcExpiry(alert['Expiry'].get('$date').get('$numberLong'))
                print('There\'s an alert with', str, 'that ends on', expiryTime)
                audio('alert.mp3')

                # u can store the time too so it knows when to prune but im a lazy cuck
                storedAlerts.append(missionID)

    return

while True:
    refresh()
    time.sleep(300)
