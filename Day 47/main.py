import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
send_to = os.getenv("SEND_TO")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
}

response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
response.raise_for_status()

amazon_website = response.text

soup = BeautifulSoup(amazon_website, "html.parser")
price = float(soup.select_one(".twisterSwatchPrice").getText().strip().replace("$", ""))

msg = EmailMessage()

msg["Subject"] = "Price of item cheaper than target!"
msg["From"] = my_email
msg["To"] = send_to
msg.set_content("Price of the item you want is cheap enough for you to buy!")

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)
