#Then, create a function that prints a 2D array in rows and columns. 
# Finally, create a program that prints three identity matrices with dimensions 
# of 3, 5 and 8. Sample result:

arr = [[], [], []]

for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i].append(0)

for i in range(len(arr)):
    arr[i][i] = 1
    print(*arr[i], sep=" ")


arr2 = [[], [], [], [], []]

for i in range(len(arr2)):
    for j in range(len(arr2)):
        arr2[i].append(0)

for i in range(len(arr2)):
    arr2[i][i] = 1
    print(*arr2[i], sep=" ")

arr3 =[[], [], [], [], [], [], [], []]

for i in range(len(arr3)):
    for j in range(len(arr3)):
        arr3[i].append(0)

for i in range(len(arr3)):
    arr3[i][i] = 1
    print(*arr3[i], sep=" ")