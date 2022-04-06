import requests
from pprint import pprint

class DataManager:
    def __init__(self):
        pass

    def get_sheet_data(self):
        # 1. Use the Sheety API to GET all the data in that sheet and print it out:
        sheet_endpoint = "https://api.sheety.co/cafd093ede58c80ca9a465f6342401de/day39FlightDeals/prices"
        response = requests.get(sheet_endpoint)
        response.raise_for_status()
        result = response.json()["prices"]
        return result


