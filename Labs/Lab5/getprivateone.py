import requests
import json
from config import config as cfg

filename = "privateone.json"

url = 'https://api.github.com/repos/YuliiaKharchenko/aprivateone'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["Forlab5"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)