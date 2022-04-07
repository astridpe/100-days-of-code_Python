from twilio.rest import Client
import smtplib

ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
MY_PHONE_NUMBER = ""

MY_EMAIL = ""
PASSWORD = ""


class NotificationManager:
    def send_message(self, price, departure_city,
                     departure_airport_code, destination_city,
                     destination_airport_code, out_time, return_time, stop_overs, via_city):
        message = f"Low price alert! Only £{price} to fly from {departure_city}-{departure_airport_code} " \
                  f"to {destination_city}-{destination_airport_code}, from {out_time} to {return_time}."

        if stop_overs > 0:
            message += f"\nFlight has {stop_overs} stop over, via {via_city}."

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER,
        )
        print(message.status)

    def send_email(self, price, departure_city,
                   departure_airport_code, destination_city,
                   destination_airport_code, out_time, return_time, stop_overs, via_city, customers):
        message = f"Low price alert! Only £{price} to fly from {departure_city}-{departure_airport_code} " \
                  f"to {destination_city}-{destination_airport_code}, from {out_time} to {return_time}." \
                  f"https://www.google.co.uk/flights?hl=en#flt={departure_airport_code}.{destination_airport_code}" \
                  f".{out_time}*{destination_airport_code}.{departure_airport_code}.{return_time}"

        if stop_overs > 0:
            message += f"\nFlight has {stop_overs} stop over, via {via_city}."

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for customer in customers:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=customer["email"],
                                    msg=f"Subject:New Low Price Flight!\n\n {message}".encode("utf-8")
                                    )
