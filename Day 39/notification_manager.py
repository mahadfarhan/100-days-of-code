import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.my_email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("EMAIL_PASSWORD")
        self.send_to = os.environ.get("SEND_TO")

    def send_email(self, city, flight_price):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.send_to,
                msg=f"Subject:Cheap flight found!\n\nBook a flight now! Flight goes to {city}, and it's price is {flight_price}",
            )
