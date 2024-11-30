#1  2  3  4  5
#2  4  6  8 10
#3  6  9 12 15
#4  8 12 16 20
#5 10 15 20 25

arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

arr[0] = [1,2,3,4,5]

for i in range(1,len(arr)):
    for j in range(0,len(arr[i])):
        arr[i][j] = 2*arr[i-1][j]

for i in range()

print(arr)

