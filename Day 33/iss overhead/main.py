import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = float(os.environ.get("MY_LAT"))
MY_LONG = float(os.environ.get("MY_LONG"))
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

nearby = False

if (
    MY_LAT >= iss_latitude - 5
    and MY_LAT <= iss_latitude + 5
    and MY_LONG >= iss_longitude - 5
    and MY_LONG <= iss_longitude + 5
):
    nearby = True

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0, "tzid": "Asia/Karachi"}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now_hr = datetime.now().hour

if nearby:
    if time_now_hr >= sunset or time_now_hr <= sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS nearby!\n\n The iss space station is currently nearby, and overhead! Look above you, it should be visible in the dark :D",
            )
