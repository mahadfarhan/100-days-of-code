import pandas as pd
import datetime as dt
import random
import os
import smtplib
from dotenv import load_dotenv

LETTER_TEMPLATES_PATH = "./birthday wisher/letter_templates"

load_dotenv()

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

df = pd.read_csv("./birthday wisher/birthdays.csv")

current_day = dt.datetime.now().day
current_month = dt.datetime.now().month

letter_list = os.listdir(LETTER_TEMPLATES_PATH)

new_df = df[(df["month"] == current_month) & (df["day"] == current_day)]

for index, row in new_df.iterrows():
    random_letter = random.choice(letter_list)
    with open(os.path.join(LETTER_TEMPLATES_PATH, random_letter)) as file:
        x = file.read()
        final_letter = x.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday!\n\n{final_letter}",
            )
