# Complete the class by adding a method print_receipt(self) that prints receipt. 
# It should contain all the information about the ride: distance, rate, and fare. 
# Then write a program in which you create two objects representing two different taxi rides.

class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km


def main():
    # your program
    ride1 = TaxiRide(2)
    ride2 = TaxiRide(3)
    fare1 = ride1.calculate_fare(10)
    fare2 = ride2.calculate_fare(12)
    print(f"Taxi 1: distance - {ride1.distance}, rate per km - {ride1.rate_per_km}, fare - {ride1.fare}")
    print(f"Taxi 2: distance - {ride2.distance}, rate per km - {ride2.rate_per_km}, fare - {ride2.fare}")

if __name__ == "__main__":
    main()
