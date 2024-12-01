# The hotel's IT system contains a list of reserved rooms. 
# The data is contained in the reservations.json file. 
# Write a program that prints the summary information as stated below. 
# Break your program into smaller parts defining functions.

import json

with open("reservations.json", "r", encoding='utf-8') as file:
    data = json.load(file)

#number of rooms

def room_number(hotel_file):
    sum = 0
    for value in hotel_file["reservations"]:
        sum += 1
    return sum
    
print(room_number(data))

#number of paid reservations
def paid(hotel_file):
    sum = 0
    for i in range(len(data["reservations"])):
        if hotel_file["reservations"][i]["paid"] == True:
            sum += 1
    return sum
    
print(paid(data))
#number of unpaid reservations
def unpaid(hotel_file):
    sum = 0
    for i in range(len(data["reservations"])):
        if hotel_file["reservations"][i]["paid"] == False:
            sum += 1
    return sum

print(unpaid(data))

#total value of paid reservations
def paid_value(hotel_file):
    sum = 0
    for i in range(len(hotel_file["reservations"])):
        if hotel_file["reservations"][i]["paid"] == True:
            sum += hotel_file["reservations"][i]["price_per_night"]*hotel_file["reservations"][i]["nights"]
    return sum

print(paid_value(data))


#total value of unpaid reservations
def unpaid_value(hotel_file):
    sum = 0
    for i in range(len(hotel_file["reservations"])):
        if hotel_file["reservations"][i]["paid"] == False:
            sum += hotel_file["reservations"][i]["price_per_night"]*hotel_file["reservations"][i]["nights"]
    return sum

print(unpaid_value(data))