import requests
from twilio.rest import Client

api_key = "f569ef028ea7bcfd1cfaa07f8f8a0539"

parameters = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

will_rain = False
for i in range(4):
    weather_id = data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

weather_condition = data["list"][0]["weather"][0]["description"]
print(weather_condition)

account_sid = "ACdc196b9763268402b443668fac625439"
auth_token = "87ca68a1effcab8d5c336c510039599c"

if will_rain:
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body="It's going to rain today. Bring an umbrella! ☂️",
        from_="+13613095450",
        to="+919324983039",
    )
    print(msg.status)

# weather_codes = [data["list"][i]["weather"][0]["id"] for i in range(4)]
# print(weather_codes)

# print(weather_id, weather_condition)
