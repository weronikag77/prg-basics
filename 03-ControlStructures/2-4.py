###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    answer = number1 + number2 
elif operator == "-":
    answer = number1 - number2
elif operator == "*":
    answer = number1 * number2
elif operator ==  "/":
    answer = number1 / number2
else: 
    print("Invalid operator")

print(f"The answer is {answer}")

