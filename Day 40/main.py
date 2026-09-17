from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data = data_manager.get_data()

user_emails_list = []
for user in data_manager.get_user_emails()["users"]:
    user_emails_list.append(user["whatIsYourEmail?"])

for item in data["prices"]:
    raw_flight_data = flight_search.check_flight_exists(item["iataCode"])
    flight_data = FlightData(raw_flight_data)
    cheapest_flight_price, cheapest_flight_stops = flight_data.find_cheapest_flight()
    if cheapest_flight_price < item["lowestPrice"]:
        data_manager.update_price(cheapest_flight_price, item["id"])
        notification_manager.send_email(
            item["city"], cheapest_flight_price, cheapest_flight_stops, user_emails_list
        )
