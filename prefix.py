# Code2040 Application - API Challenge Step 4
# Given a prefix and an array, return a new array with only the values that don't begin with the prefix

import requests
import json

r = requests.post("http://challenge.code2040.org/api/prefix", data = {'token':''}) # Removed token to protect privacy

jsonData = r.json()

prefix = jsonData['prefix']
originalArray = jsonData['array']
newArray = []

for item in originalArray:
    if not (item.startswith(prefix)):
        newArray.append(item)

r = requests.post("http://challenge.code2040.org/api/prefix/validate", data = {'token':'', 'array':json.dumps(newArray)}) # Removed token to protect privacy

print r.text