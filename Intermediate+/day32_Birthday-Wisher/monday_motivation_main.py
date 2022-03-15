import random
import smtplib
import datetime as dt
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_OTHER_EMAIL = os.environ.get("MY_OTHER_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as data:
        quotes_list = data.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n {random_quote}"
                            )








