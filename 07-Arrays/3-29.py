
#Create a program that calculates the sum of values in the last column.

arr = [[7,3,7,9,0], [2,9,0,1,5], [3,8,6,4,7], [8,7,1,1,5]]

sum = 0
for row in arr:
    sum += row[len(row)-1]
print(sum)