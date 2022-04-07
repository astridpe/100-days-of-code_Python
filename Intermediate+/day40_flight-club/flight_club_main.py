import requests
import os

API_KEY = os.environ['API_KEY']
SHEET_ENDPOINT = ""

print("Welcome to Astrid's Flight Club.\nWe find the best flight deals and email you.")

first_name = input("What is your first name? \n")
last_name = input("What is your last name? \n")
email = input("What is your email? \n")

not_correct_email = True

while not_correct_email:
    verify_email = input("Type your email again \n")

    if verify_email == email:
        not_correct_email = False

print("You're in the club!")

new_data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}

response = requests.post(url=SHEET_ENDPOINT, json=new_data)
print(response.text)
