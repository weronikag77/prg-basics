#Then, create a program that prints transposed matrices, in rows and columns, for the following matrices.

# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3 4 5
# 6 7 8 9 0

# 5 6 7 8

arr = [[1,2,3], [4,5,6], [7,8,9]]
arr2 = [[], [], []]

for i in range(len(arr)):
    for j in range(len(arr)):
        n1 = arr[i][j]
        arr2[j].append(n1)

for i in range(len(arr2)):
    print(*arr2[i], sep=" ")
print(" ")

arr = [[1,2,3,4,5], 
       [6,7,8,9,0]]
arr2 = [[], [], [], [], []]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        n1 = arr[i][j]
        arr2[j].append(n1)

for i in range(len(arr2)):
    print(*arr2[i], sep=" ")
print(" ")

arr = [5,6,7,8]
arr2 = [[],[],[],[]]

for i in range(len(arr)):
    n1 = arr[i]
    arr2[i].append(n1)

for i in range(len(arr2)):
    print(*arr2[i], sep=" ")
print(" ")
