import json
import re

json_data = open('All.json', encoding='utf8')
data = json.load(json_data)

bigassdict = {}
justsayno = ['name','imageName','tradable','drops','patchlogs','components']

def filterDT(desc):
	sentence = []
	
	for i in desc.split('<'):
		sentence.append(i.split('>')[-1])
	
	return ''.join(sentence)

def replaceStat(filteredDesc, maxLevel):
	return re.sub('\d[.\d]*',lambda x: str(round(float(x.group(0)) * (maxLevel+1),1)),filteredDesc)

for i in data:
	bigassdict[i['name']] = {}
	
	for j in i:
		if j not in justsayno:
			bigassdict[i['name']][j] = i.get(j)
			
	if i['category'] == 'Mods' and 'Riven' not in i['name']:

		modDesc = filterDT(i['description'])
		modMax = i['fusionLimit']
		
		bigassdict[i['name']]['description'] = replaceStat(modDesc, modMax)
		
with open('test.json','w') as outfile:
	json.dump(bigassdict,outfile,indent=4, sort_keys=True)
	


