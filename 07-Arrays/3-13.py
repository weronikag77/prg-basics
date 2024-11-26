#Define a function occurs(number, array) that returns True if a given number is present in an array.
#Then create a program that checks whether the number entered from the keyboard is present 
#in the array [15, 38, 7, 23, 14]. Sample result:

#Number: 23
#Array: 15 38 7 23 14
#Result: number 23 appears in the array

arr = [15,38,7,23,14]
num = int(input("Enter a number: "))

def occurs(number, array):
    if number in array: 
        return True
    else:
        return False

if occurs(num,arr) == True:
    print("Number:", num)
    print("Array: ", arr)
    print(f"Result: number {num} appears in the array")
else:
    print("Number:", num)
    print("Array: ", arr)
    print(f"Result: number {num} does not appear in the array")