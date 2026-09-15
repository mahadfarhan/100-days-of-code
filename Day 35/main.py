import os
from dotenv import load_dotenv
import requests
import smtplib

load_dotenv()

API_KEY = os.getenv("API_KEY")

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")
send_to = os.environ.get("SEND_TO")

parameters = {
    "lat": 33.51834737860585,
    "lon": 73.08683940976648,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters
)

response.raise_for_status()
weather_data = response.json()

will_rain = False
for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to,
            msg=f"Subject:Bring Umbrella!\n\nBring an umbrella, it's gonna rainnn",
        )
