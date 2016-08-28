# Code2040 Application - API Challenge Step 4
# Given a prefix and an array, return a new array with only the values that don't begin with the prefix

import requests
import json

myData = {'token':''} # Removed token to protect privacy
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post("http://challenge.code2040.org/api/prefix", data = json.dumps(myData), headers = headers)

jsonData = r.json()

prefix = jsonData['prefix']
originalArray = jsonData['array']
newArray = []

for item in originalArray:
    if not (item.startswith(prefix)):
        newArray.append(item)

myData = {'token':'', 'array':newArray} # Removed token to protect privacy

r = requests.post("http://challenge.code2040.org/api/prefix/validate", data = json.dumps(myData), headers = headers) 

print r.text