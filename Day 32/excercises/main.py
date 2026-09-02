import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os

# now = dt.datetime.now()
# year = now.year
# print(year)

# date_of_birth = dt.datetime(year=2004, month=9, day=11)

with open("quotes.txt") as file:
    list_of_quotes = file.read().splitlines()

load_dotenv()

send_to = os.environ.get("SEND_TO")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

today = dt.datetime.now().weekday()

if today == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to,
            msg=f"Subject:Monday Motivation!\n\n{random.choice(list_of_quotes)}",
        )
