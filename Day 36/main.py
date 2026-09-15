import requests
from dotenv import load_dotenv
import os
import smtplib
import json
from email.message import EmailMessage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
SEND_TO = os.environ.get("SEND_TO")

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("APIKEY"),
}

response = requests.get("https://www.alphavantage.co/query?", params=params)
response.raise_for_status()

tsla_data = response.json()

# with open("local_json_for_testing.json", "w") as file:
#     json.dump(tsla_data, file)

# with open("local_json_for_testing.json", "r") as file:
#     tsla_data = json.load(file)

tsla_list = list(tsla_data["Time Series (Daily)"].items())[:2]
price_list = []

for item in tsla_list:
    price_list.append(float(item[1]["4. close"]))

price_change = ((price_list[0] - price_list[1]) / price_list[1]) * 100

if price_change < 0:
    arrow = "🔻"
else:
    arrow = "🔺"

price_change = abs(price_change)

news_params = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": os.getenv("NEWSAPI"),
}

msg = EmailMessage()

if price_change >= 5:
    news_response = requests.get(
        "https://newsapi.org/v2/everything?", params=news_params
    )
    news_response.raise_for_status()

    news_data = news_response.json()

    news_list = news_data["articles"][:3]

    empty_string = ""

    for item in news_list:
        headline = item["title"]
        brief = item["description"]
        empty_string += "Headline: " + headline + "\n" + "Brief: " + brief + "\n\n\n"

    msg["Subject"] = f"{STOCK}: {arrow}{round(price_change, 2)}%"
    msg["From"] = MY_EMAIL
    msg["To"] = SEND_TO
    msg.set_content(empty_string)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(msg)
