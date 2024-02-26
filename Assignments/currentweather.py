


import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_direction_10m"
response = requests.get(url)
# print(response.json())
data = response.json()

'''
with open ("Weather", "w") as fp: 
    json.dump(data,fp)
'''

current = data["current"]
Curtemp = current ["temperature_2m"]
Winddir = current ["wind_direction_10m"]


units = data["current_units"]
celsuis = units["temperature_2m"]
unitwd = units[ "wind_direction_10m"]

print("The current temperature is {}{}\n" "The current wind direction(10 m) is {}{}".format(Curtemp, celsuis, Winddir, unitwd))