#[[-38, 19], [5,40],[-7,11],[29,16]]
#Create a program that finds the smallest and largest values 
#in the array and in which row and column they are located.
import numpy as np

arr = np.array([[-38, 19], 
       [5,40],
       [-7,11],
       [29,16]])

minimum = 0
maximum = 0


for i in range(0, len(arr)):
    for j in range(0,len(arr[i])):
        if arr[i][j] < minimum:
            minimum = arr[i][j]
        elif arr[i][j] > maximum:
            maximum = arr[i][j]
        else:
            minimum = minimum
            maximum = maximum

print(np.where(arr==minimum))
print(np.where(arr==maximum))
