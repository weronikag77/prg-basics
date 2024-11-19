###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = 'shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:
        content = file.write(product_name)
    return content

file_name = shopping_list
product = 1
product_name = product

while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break # stops entering food names ('while' breaks)
    else:
        add_product(shopping_list, product)

