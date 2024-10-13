#Vehicle registration numbers in Krakow start with the letters KR or KK. 
#Write a program that checks whether the vehicle registration number entered 
# from the keyboard means a vehicle from Krakow. Display True whether a car is from Krakow or False otherwise.
registration_number = input('Enter the registration number: ')
from_krakow = registration_number[0:2] == 'KR' or registration_number[0:2] == 'KK'
print(f'Car is from Krakow: {from_krakow}')