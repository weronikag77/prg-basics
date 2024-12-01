#Write a program that calculates and displays the average price for 
# a room in hotels in Krakow and Sopot 
# and indicates in which cities hotels are cheaper. Sample result:

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    list = []
    for i in range(len(hotels)):
        list.append(hotels[i]["name"])
    return list

def avg_price(hotels):
    sum = 0
    for i in range(len(hotels)):
        sum += hotels[i]["price"]
    avg = sum/len(hotels)
    return avg

print(f"Hotels in Krakow: ", end="")
print(*hotel_list(hotels_in_Krakow), sep=", ")
print(f"Average hotel price in Krakow: {avg_price(hotels_in_Krakow)}")
print(f"Hotels in Sopot: ", end="")
print(*hotel_list(hotels_in_Sopot), sep=", ")
print(f"Average hotel price in Sopot: {avg_price(hotels_in_Sopot)}")