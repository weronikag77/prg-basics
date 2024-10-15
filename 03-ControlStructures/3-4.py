###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter the first number: '))
y = int(input("Enter the second number: "))

if not x < 0 or not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f"Both numbers are negative")