#An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints the 
#array and the arithmetic mean of array values. 
#Use the “while” loop statement.

arr = [15,8,31,47,2,19]

i = 0
sum = 0
while i < len(arr):
    sum += arr[i]
    i+= 1

mean = sum/len(arr)
print("Arithmetic mean: ",mean)