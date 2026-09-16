import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "mahadbinfarhan"
TOKEN = os.getenv("AUTH_TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "NotMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "studying",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours have you studied today?"),
}

# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(response.text)

PIXEL_UPDATE_ENDPOINT = (
    f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
)

pixel_update_config = {"quantity": "5"}

# response = requests.put(
#     url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_config, headers=headers
# )
# print(response.text)

PIXEL_DELETE_ENDPOINT = (
    f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
)

# response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
# print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}"

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)
