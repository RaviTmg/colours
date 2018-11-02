import requests, json, csv

url = "http://www.colourlovers.com/api/palettes/top?format=json&numResults=100"
r = requests.get(url)
print(r.json())