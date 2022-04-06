import requests
from pprint import pprint

SHEET_ENDPOINT = "https://api.sheety.co/cafd093ede58c80ca9a465f6342401de/day39FlightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        # 1. Use the Sheety API to GET all the data in that sheet and print it out:
        response = requests.get(SHEET_ENDPOINT)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(self.destination_data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_sheet_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)





