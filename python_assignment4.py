import numpy as np

class FlightTable:
    def __init__(self, data):
        self.data = np.array(data, dtype=[('flight_id', 'U10'), ('origin', 'U3'), ('destination', 'U3'), ('price', 'i4')])

    def search_flights_for_city(self, city):
        mask =(self.data['destination'] == city)
        return self.data[mask]

    def search_flights_from_city(self, city):
        mask = self.data['origin'] == city
        return self.data[mask]

    def search_flights_between_cities(self, origin, destination):
        mask = (self.data['origin'] == origin) & (self.data['destination'] == destination)
        return self.data[mask]

data = [("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)]

flight_table = FlightTable(data)


print("Enter the search parameter:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")
print("Enter your Choice: ")
choice = int(input())

if choice == 1:
    city = input("Enter the city: ")
    results = flight_table.search_flights_for_city(city)
elif choice == 2:
    city = input("Enter the city: ")
    results = flight_table.search_flights_from_city(city)
elif choice == 3:
    origin = input("Enter the origin city: ")
    destination = input("Enter the destination city: ")
    results = flight_table.search_flights_between_cities(origin, destination)
else:
    print("Invalid choice")
    results = []

for result in results:
    print(result)
