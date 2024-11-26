# Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that prints the numbers from the first array 
# that do not appear in the second array.

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
arr3 = [ ]

for item in arr1:
    if item not in arr2:
        arr3.append(item)

print(arr3)