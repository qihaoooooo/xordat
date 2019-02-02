#
#   Strip items from wf-all.json
#

import json
import re

# remove icon tags of form <...> from description
def remove_icons(str):
    return re.sub(r"<.+>", "", str)

# calculate status at maximum rank rounded to 1 d.p.
def max_stat(base, max_rank):
    return round(base * (max_rank + 1), 1)

# replaces status numbers to status at max rank
def replace_stat(filtered_desc, max_rank):

    # WHAT IS GOING ON HERE
    return re.sub(r"\d[.\d]*", lambda x: max_stat(float(x), max_rank),
        filtered_desc)

    return re.sub('\d[.\d]*',lambda x: str(round(float(x.group(0)) * (maxLevel+1),1)),filteredDesc)
    # ?????

with open("all.json", encoding="utf8") as all_json:
    data = json.load(all_json)

# JSON keys to drop
reject = ['name', 'imageName', 'tradable', 'drops', 'patchlogs', 'components']
filtered = {}

for i in data:
    bigassdict[i['name']] = {}

    for j in i:
        if j not in justsayno:
            bigassdict[i['name']][j] = i.get(j)

    if i['category'] == 'Mods' and 'Riven' not in i['name']:

        modDesc = filterDT(i['description'])
        modMax = i['fusionLimit']

        bigassdict[i['name']]['description'] = replaceStat(modDesc, modMax)

# export filtered list as JSON file
with open("filtered.py", "w") as outfile:
    json.dump(filtered, outfile, indent=4, sort_keys=True)
