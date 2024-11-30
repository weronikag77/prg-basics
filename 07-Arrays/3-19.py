#Write a program that, for the given array of real numbers, prints 
#the number of elements that are greater than the given value entered from the keyboard.

arr = [1,2,6,7,4]

number = int(input("Enter a number: "))

sum = 0
for item in arr:
    if item > number:
        sum += 1

print(f"Number of elements greater than {number}: {sum}")