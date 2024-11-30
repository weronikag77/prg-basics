price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

#prints a list of products and their prices before the discount
list = []
for item in price_list.items():
    list.append(item)

print(list)
#prints the total value of the products before the discount
sum  = 0
for key, value in price_list.items():
    sum += value

print(sum)
#modifies the price list according to the discount (round prices to two decimal places)
for key, value in price_list.items():
    value2 = value*0.9
    value2 = round(value2,2)
    price_list[key] = value2
    
#prints a list of products and their prices after the 10% discount
print(price_list)
#prints the total value of the products after the discount
sum  = 0
for key, value in price_list.items():
    sum += value
