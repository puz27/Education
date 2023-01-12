import requests
import json
resp = requests.get('https://www.jsonkeeper.com/b/3QJZ')
data = resp.json()
[print(i) for i in data]