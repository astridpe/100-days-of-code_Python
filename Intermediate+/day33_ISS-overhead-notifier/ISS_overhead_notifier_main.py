import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 59.911321
MY_LNG = 10.740508
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_OTHER_EMAIL = os.environ.get("MY_OTHER_EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    MY_LAT_range = [MY_LAT + 5, MY_LAT, MY_LAT - 5]
    MY_LNG_range = [MY_LNG + 5, MY_LNG, MY_LNG - 5]

    if iss_latitude in MY_LAT_range and iss_longitude in MY_LNG_range:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour

    print(sunset)
    print(sunrise)

    if hour_now >= sunset or hour_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_OTHER_EMAIL,
                                msg="Subject: Look Up👆\n\n The ISS is above you in the sky."
                                )






