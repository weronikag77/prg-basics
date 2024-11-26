#An array contains integer numbers: 2, 6, 4, 9, 7. Create a program that prints the array values graphically as below. Define a function star(n) 
#that returns the given number of asterisks as a string. 
#Use a defined function in the program.

def f(array):
    for i in range(len(array)):
        print(array[i], ":", "*"*array[i])


arr = [2,6,4,9,7]
print(f(arr))