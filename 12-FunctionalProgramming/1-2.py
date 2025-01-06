a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

mean = lambda x,y: (x+y)/2

print(f"The arithmetic mean of the numbers is {mean(a,b)}")