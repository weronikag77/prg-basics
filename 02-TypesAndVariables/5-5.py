#Display the product price, discount, discounted product price, and the difference between the product price before and after the discount.
price = float(input('Enter the price: '))
price = round(price, 2)
discount = float(input('Enter discount %: '))
discount = discount/100
discounted_price = price - discount*price
discounted_price = round (discounted_price, 2)
price_difference = price - discounted_price
price_difference = round (price_difference, 2)
print(f'Product price: {price}')
print(f'Discount %: {discount}')
print(f'Discounted price: {discounted_price}')
print(f'Price difference: {price_difference}')