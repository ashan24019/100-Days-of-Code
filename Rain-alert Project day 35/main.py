import requests

parameters = {
    "lat" : 6.705574,
    "lon" : 80.384735,
    "appid" : "3046154e9fae10a676cb5586084292a4"
}


response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

