from data_manager import DataManager
from flight_search import FlightSearch

# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for data in sheet_data:
        data["iataCode"] = flight_search.get_iataCode(data["city"])

print(f"sheet_data:\n {sheet_data}")
data_manager.destination_data = sheet_data
data_manager.update_sheet_data()
