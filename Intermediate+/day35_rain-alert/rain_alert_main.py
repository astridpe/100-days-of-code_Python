import requests
import os
from twilio.rest import Client

# Oslo:
MY_LAT = 59.911321
MY_LNG = 10.740508

# # Frankfurt:
# MY_LAT = 50.110924
# MY_LNG = 8.682127

MY_API_KEY = os.environ.get("MY_API_KEY")
print(os.environ.get('TWILIO_PHONE_NUMBER'))
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()
first_id = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella ☂️",
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
    print(message.status)
