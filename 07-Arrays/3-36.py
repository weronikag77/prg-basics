#Create a function that convert two-dimensional (2D) array into 1D. 
# Then create a program that prints 1D array for the following 2D arrays.

#2 3
#1 5

#5 0 3 7 5
#9 0 9 1 2

#2 1
#3 5
#7 4
#2 6

arr = [[2,1], [3,5], [7,4], [2,6]]
arr2 = []

def one_dimension(array, array2):
    for i in range(len(array)):
        for j in range(len(array[0])):
            array2.append(array[i][j])
    return array2

print(one_dimension(arr,arr2))