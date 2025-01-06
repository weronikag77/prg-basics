# Define a function that calculates the arithmetic mean of two numbers. 
# Then, write a program that takes two integer numbers from the keyboard 
# and calculates their arithmetic mean.

def mean(a,b):
    sum = a + b
    mean = sum/2
    return mean

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(mean(a,b))