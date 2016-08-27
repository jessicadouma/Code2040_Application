import requests

def reverseString(orginalWord):
    reversedWord = ""
    for char in reversed(orginalWord):
        reversedWord += char
    return reversedWord

r = requests.post("http://challenge.code2040.org/api/reverse", data = {'token':'cdde5bd0ed405c44f3398c153604e69d'})

originalWord = r.text
reversedWord = reverseString(originalWord)

r = requests.post("http://challenge.code2040.org/api/reverse/validate", data = {'token':'cdde5bd0ed405c44f3398c153604e69d', 'string':reversedWord})

print r.text