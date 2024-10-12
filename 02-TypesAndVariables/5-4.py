#
amount = float(input("Enter the amount: "))
amount = round(amount, 2)
vat = amount*0.23
vat = round(vat, 2)
print(f'Amount: {amount}')
print(f'VAT: {vat}')
