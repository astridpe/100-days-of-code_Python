import requests

SHEET_ENDPOINT = ""
SHEET_ENDPOINT_CUSTOMERS = ""

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        response = requests.get(SHEET_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_sheet_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_data(self):
        response = requests.get(SHEET_ENDPOINT_CUSTOMERS)
        self.destination_data = response.json()["users"]
        return self.destination_data


