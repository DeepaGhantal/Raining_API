import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key= "754439bb7097b200795ea86c5352267e"
api_key= os.environ.get("OWM_API_KEY")
account_sid = 'AC77e478642866db645b48967e8ec31b99'
auth_token = os.environ.get("AUTH_TOKEN")
# auth_token = '7ba5219610e0a687ac785814845b8a4a'

parameters = {
    "lat":13.769040,
    "lon":109.228371,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
# print(response.status_code
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+15416481020',
        to='+918660234491'
    )

    print(message.status)