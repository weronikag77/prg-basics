#An array contains numbers: -15, 8, -31, 47, -2, 19. Create a 
#program that finds and prints the maximum and minimum number. 
#Do not use available functions.

arr = [-15,8,-31,47,-2,19]

min = arr[0]
for i in range(0, len(arr)):
    if arr[i] < min:
        min = arr[i]

max = arr[0]
for i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]

print(min)
print(max)