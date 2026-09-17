import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.my_email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("EMAIL_PASSWORD")

    def send_email(self, city, flight_price, num_stops, recipients):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            msg = EmailMessage()
            msg["Subject"] = "Cheap flight found!"
            msg["From"] = self.my_email
            msg["Bcc"] = ", ".join(recipients)
            msg["To"] = self.my_email
            msg.set_content(
                f"Book a flight now! Flight goes to {city}, and its price is {flight_price}, with total stops {num_stops}"
            )
            connection.send_message(msg)
