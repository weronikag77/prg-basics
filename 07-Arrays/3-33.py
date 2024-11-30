# A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Print array values in rows and columns before and after changes.

arr = [[1,2,3,4,5], 
    [6,7,8,9,10], 
    [11,12,13,14,15]]

for i in range(0, len(arr)):
    column1 = arr[i][0]
    column2 = arr[i][len(arr[i])-1]
    arr[i][0] = column2
    arr[i][len(arr[i])-1] = column1

print(arr)