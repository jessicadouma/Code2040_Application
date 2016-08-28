# Code2040 Application - API Challenge Step 5
# Given a date and time interval, return the resulting date

import requests
import datetime

r = requests.post("http://challenge.code2040.org/api/dating", data = {'token':''}) # Removed token to protect privacy

jsonData = r.json()

datestamp = jsonData['datestamp']
interval = jsonData['interval']

originalDatestamp = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
incrDatestamp = originalDatestamp + datetime.timedelta(0,interval)
incrDatestamp = incrDatestamp.isoformat() + 'Z'

r = requests.post("http://challenge.code2040.org/api/dating/validate", data = {'token':'', 'datestamp':incrDatestamp}) # Removed token to protect privacy

print r.text