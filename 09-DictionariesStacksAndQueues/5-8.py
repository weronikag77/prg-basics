#Write a program to calculate the total cost of a shopping cart using a price list.

# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
dictionary = {

}
for key, value in prices.items():
    if key in cart:
        dictionary[key] = cart[key]*prices[key]

print(dictionary)