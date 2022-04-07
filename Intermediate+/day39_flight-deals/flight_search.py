import requests
from flight_data import FlightData

API_KEY = ""
FLIGHT_SEARCH_ENDPOINT = ""


class FlightSearch:

    def get_iataCode(self, city_name):
        location_endpoint = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        headers = {
            "apikey": API_KEY,
        }
        response = requests.get(url=location_endpoint, params=parameters, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{FLIGHT_SEARCH_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1

            response = requests.get(
                url=f"{FLIGHT_SEARCH_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )

            try:
                data = response.json()["data"][0]
            except IndexError:
                return None

            else:
                flight_data = FlightData(
                    price=data["price"],
                    departure_city=data["route"][0]["cityFrom"],
                    departure_airport_code=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport_code=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                departure_airport_code=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport_code=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=0,
                via_city=data["route"][0]["cityTo"]
            )

            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
