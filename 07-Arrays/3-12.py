#Create a program that prints all unique elements in an array. Sample result:

#Array: 2 3 2 5 8 1 9 8
#Unique elements: 3 5 1 9

arr = [2,3,2,5,8,1,9,8]
arr2 = []

for item in arr:
    if arr.count(item) == 1:
        arr2.append(item)

print(arr2)
