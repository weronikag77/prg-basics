#Write a program that takes data from the keyboard about a purchased product:

#name
#price (real number with two decimal places)
#paid (yes/no)
#The program then saves the product data in the product.json file.

import json

dictionary = {

}

name = input("Enter a name: ")
dictionary["name"] = name
price = float(input("Enter the price: "))
dictionary["price"] = price
paid = (input("Is it paid for? (yes/no): "))
if paid == "yes":
    paid = True
elif paid == "no":
    paid = False
dictionary["paid"] = paid

json_file = "product.json"

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(dictionary, file, indent=4)

