import random
import smtplib
import datetime as dt
import pandas
import os


MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    random_number = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_number}.txt"

    with open(file_path) as data:
        letter_contents = data.read()
        new_letter = letter_contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n {new_letter}"
                            )


