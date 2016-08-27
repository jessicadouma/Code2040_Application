# Code2040 Application - API Challenge Step 2
# Given a string and an array of strings, return the index of the string

import requests
import json

r = requests.post("http://challenge.code2040.org/api/haystack", data = {'token':''}) # Removed token to protect privacy

jsonData = r.json()

needle = jsonData['needle']
haystack = jsonData['haystack']

index = haystack.index(needle)

r = requests.post("http://challenge.code2040.org/api/haystack/validate", data = {'token':'', 'needle':index}) # Removed token to protect privacy

print r.text