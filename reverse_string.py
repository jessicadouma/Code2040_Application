# Code2040 Application - API Challenge Step 2
# Reverse a string

import requests

def reverseString(orginalWord):
    reversedWord = ""
    for char in reversed(orginalWord):
        reversedWord += char
    return reversedWord

r = requests.post("http://challenge.code2040.org/api/reverse", data = {'token':''}) # Removed token to protect privacy

originalWord = r.text
reversedWord = reverseString(originalWord)

r = requests.post("http://challenge.code2040.org/api/reverse/validate", data = {'token':'', 'string':reversedWord}) # Removed token to protect privacy

print r.text