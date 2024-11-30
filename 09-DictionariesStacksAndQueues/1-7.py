#Write a program that prints:

#a list of products and the quantity
#the total number of products in the store

products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

list = []
for item in products.items():
    list.append(item)

print(list)

sum = 0
for key, value in products.items():
    sum += value

print(sum)
