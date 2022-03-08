import random
import smtplib
import datetime as dt

MY_EMAIL = "astridtesting282@gmail.com"
PASSWORD = "catZaw1?#"

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
                            to_addrs="astridtesting282@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n {random_quote}"
                            )








