###
# A program that reads a SWIFT code from the keyboard
# and displays the bank code and country code.
#Bank Code (4 characters)
#Country Code (2 characters)
#Location Code (2 characters)
swift = input("Enter SWIFT code: ")
bank_code = swift[0:4]
country_code = swift[4:6]
location_code = swift[6:8]
print(f"Bank code: {bank_code}")
print(f"Country code: {country_code}")
print(f"Location code: {location_code}")