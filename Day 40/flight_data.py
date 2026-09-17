class FlightData:
    def __init__(self, raw_data):
        self.flights = raw_data["flights"]

    def find_cheapest_flight(self):
        for flight in self.flights:
            if flight["cheapest_flight"]:
                self.cheapest_flight = flight
                cheapest_flight_string = ""
                if self.cheapest_flight["number_of_stops"] == 0:
                    cheapest_flight_string = "nonstop"
                elif self.cheapest_flight["number_of_stops"] == 1:
                    cheapest_flight_string = "1 stop"
                else:
                    cheapest_flight_string = "2 stops"
                return (
                    self.cheapest_flight["price"],
                    cheapest_flight_string,
                )
