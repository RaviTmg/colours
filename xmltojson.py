import xmltodict, json
import requests
import xml.etree.ElementTree as ET

url = "http://www.colourlovers.com/api/palettes/top"
r = requests.get(url)
root = ET(r.content)
print("results: ",root.attrib["numResults"])
for palette in root.iter("palette"):
    pass
    
# o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')

# with open('jsonfiles/palettes/top.json', 'w') as outfile:
#     json.dump(r.content,outfile)