from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data = data_manager.get_data()

for item in data["sheet1"]:
    flight_data = flight_search.get_data(item["iataCode"])
    flight_data = FlightData(flight_data)
    cheapest_flight_price = flight_data.find_cheapest_flight()
    if cheapest_flight_price < item["lowestPrice"]:
        notification_manager.send_email(item["city"], cheapest_flight_price)
