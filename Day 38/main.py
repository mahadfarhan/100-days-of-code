import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

X_APP_ID = os.getenv("X-APP-ID")
X_APP_KEY = os.getenv("X-APP-KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

exercise_headers = {"x-app-id": X_APP_ID, "x-app-key": X_APP_KEY}

query = input("What did you do today? ")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_params = {"query": query, "weight_kg": 45, "age": 22, "gender": "male"}

response = requests.post(
    url=exercise_endpoint, json=exercise_params, headers=exercise_headers
)
response.raise_for_status()
data = response.json()
today = datetime.now()


sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["name"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}

sheet_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheet_headers)
response.raise_for_status()
print(response.text)
