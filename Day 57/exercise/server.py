from flask import Flask, render_template
import random
import datetime as dt
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

APIKEY = os.getenv("APIKEY")


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    parameters = {"name": name, "apikey": APIKEY}

    response = requests.get("https://api.agify.io", params=parameters)
    response.raise_for_status()

    age_data = response.json()

    response = requests.get("https://api.genderize.io", params=parameters)
    response.raise_for_status()

    gender_data = response.json()
    return render_template(
        "guess.html", guess_name=name, age=age_data["age"], gender=gender_data["gender"]
    )


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
