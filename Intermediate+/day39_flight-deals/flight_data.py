import datetime as dt

TOMORROW = (dt.date.today() + dt.timedelta(days=1))
SIX_MONTHS = TOMORROW + dt.timedelta(days=(6 * 30))

class FlightData:
    def __init__(self):
        self.price
        self.departure_airport_code
        self.departure_city
        self.curr = "GBP"
        self.date_from = TOMORROW.strftime("%d/%m/%Y")
        self.date_to = SIX_MONTHS.strftime("%d/%m/%Y")
