###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#input: temperature in C
#calculate to F
#calculate to K
#display both
temp_C = float(input('Enter temperature in Celsius: '))
temp_F = temp_C*1.8 + 32
temp_K = temp_C + 273.15

print(f'Temperature in Celsius: {temp_C}')
print(f'Temperature in Fahrenheit: {temp_F}')
print(f'Temperature in Kelvin: {temp_K}')