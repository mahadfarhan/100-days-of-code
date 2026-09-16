import requests_cache
from dotenv import load_dotenv
import os

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


class DataManager:
    def __init__(self):
        self.session = requests_cache.CachedSession("sheety_cache", expire_after=6000)
        self.SHEETY_HEADER = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    def get_data(self):
        self.response = self.session.get(
            url=SHEETY_ENDPOINT, headers=self.SHEETY_HEADER
        )
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data
