import requests_cache
from dotenv import load_dotenv
import os

load_dotenv()

SERP_ENDPOINT = "https://serpapi.com/search"
SERP_API = os.getenv("SERP_API_KEY")


class FlightSearch:
    def __init__(self):
        self.session = requests_cache.CachedSession("serp_cache", expire_after=6000)

    def get_data(self, arrival_id):
        serp_params = {
            "type": 1,
            "month": 0,
            "travel_duration": 2,
            "engine": "google_travel_explore",
            "api_key": SERP_API,
            "departure_id": "ISB",
            "arrival_id": arrival_id,
        }
        self.response = self.session.get(url=SERP_ENDPOINT, params=serp_params)
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data
