import json 

# reads from the json file we created
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    if 'obama' in i['tweet'].lower():
        print(i['tweet'])
