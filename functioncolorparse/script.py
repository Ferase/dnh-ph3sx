import json

with open('../server/src/dictionary/files/functions.json', 'r') as json_file:
    json_data = json.load(json_file) # Input is list of dict. So,load everything

sourceFile = open('out.txt', 'w')

for json_i in json_data:
    print(json_i.get('name', ''), file = sourceFile)

sourceFile.close()