import requests

API_KEY = ""
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_iataCode(self, city_name):
        parameters = {
            "term": city_name
        }
        headers = {
            "apikey": API_KEY,
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=parameters, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code







