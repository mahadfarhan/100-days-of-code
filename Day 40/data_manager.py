import requests_cache
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class DataManager:
    def __init__(self):
        self.BEARER_TOKEN = os.getenv("BEARER_TOKEN")
        self.SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
        self.session = requests_cache.CachedSession("sheety_cache", expire_after=6000)
        self.SHEETY_HEADER = {"Authorization": f"Bearer {self.BEARER_TOKEN}"}

    def get_data(self):
        self.response = self.session.get(
            url=self.SHEETY_PRICES_ENDPOINT, headers=self.SHEETY_HEADER
        )
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data

    def update_price(self, new_flight_price, row_id):
        new_url = f"{self.SHEETY_PRICES_ENDPOINT}/{row_id}"
        update_params = {"price": {"lowestPrice": new_flight_price}}
        response = requests.put(
            url=new_url, json=update_params, headers=self.SHEETY_HEADER
        )
        response.raise_for_status()

    def get_user_emails(self):
        self.response = self.session.get(
            url=self.SHEETY_USERS_ENDPOINT, headers=self.SHEETY_HEADER
        )
        self.response.raise_for_status()
        return self.response.json()
