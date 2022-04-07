from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

TOMORROW = (dt.date.today() + dt.timedelta(days=1))
SIX_MONTHS_FROM_TODAY = TOMORROW + dt.timedelta(days=(6 * 30))
ORIGIN_CITY_IATA_CODE = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_search.get_iataCode(data["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_sheet_data()

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA_CODE,
        destination["iataCode"],
        from_time=TOMORROW,
        to_time=SIX_MONTHS_FROM_TODAY
    )
    try:
        if destination["lowestPrice"] > flight.price:
            notification_manager.send_message(flight.price,
                                              flight.departure_city,
                                              flight.departure_airport_code,
                                              flight.destination_city,
                                              flight.destination_airport_code,
                                              flight.out_date,
                                              flight.return_date, flight.stop_overs, flight.via_city)

            customers = data_manager.get_customer_data()
            notification_manager.send_email(flight.price,
                                            flight.departure_city,
                                            flight.departure_airport_code,
                                            flight.destination_city,
                                            flight.destination_airport_code,
                                            flight.out_date,
                                            flight.return_date, flight.stop_overs, flight.via_city, customers)

    except AttributeError:
        continue



