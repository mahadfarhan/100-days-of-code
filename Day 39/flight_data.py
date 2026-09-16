class FlightData:
    def __init__(self, raw_data):
        self.flights = raw_data["flights"]

    def find_cheapest_flight(self):
        for flight in self.flights:
            if flight["cheapest_flight"]:
                self.cheapest_flight = flight
                return self.cheapest_flight["price"]
