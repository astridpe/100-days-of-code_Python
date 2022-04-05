import requests
import datetime as dt
import os

GENDER = "female"
WEIGHT_KG = 57
HEIGHT_CM = 168
AGE = 28

API_KEY = os.environ["APP_KEY"]
APP_ID = os.environ["APP_ID"]
TOKEN = os.environ["TOKEN"]


TODAY = dt.datetime.now().strftime("%d/%m/%Y")
TIME = dt.datetime.now().strftime("%X")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()["exercises"][0]

row_data = {
    "workout": {
        "date": TODAY,
        "time": TIME,
        "exercise": result["name"].title(),
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}

bearer_headers = {
    "Authorization": TOKEN
}

sheet_response = requests.post(sheet_endpoint, json=row_data, headers=bearer_headers)

print(sheet_response.text)



