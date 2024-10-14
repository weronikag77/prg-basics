###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input("Enter the distance in km: "))
fuel_price = float(input("Enter the fuel price per 1 liter: "))
fuel_consumption = float(input("Enter the fuel consumption in liters per 100 km: "))
total_fuel_consumption = fuel_consumption*distance/100
total_cost = total_fuel_consumption*fuel_price
print(f"Total cost: {total_cost}")