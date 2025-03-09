import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "3046154e9fae10a676cb5586084292a4"

parameters = {
    "lat" : 6.705574,
    "lon" : 80.384735,
    "appid" : api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")


