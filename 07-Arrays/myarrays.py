#Create a module MyArrays containing functions to operate on an array of numbers:

#A function that returns the second largest element in an array
#A function that returns the difference between the largest and smallest values in an array
#A function that returns the median of numbers in an array.

def second_largest(array):
    array.sort()
    return array[len(array)-2]

def difference(array):
    array.sort()
    return array[len(array) - 1] - array[0]

def median(array):
    array.sort()
    n = len(array)//2
    if len(array)%2 == 0:
        median = (array[n-1]+array[n])/2
    else:
        median = array[n]
    return median

print(second_largest([1,9,6,8]))
print(median([1,2,3,4,5]))

#Smallest and largest number: 2,8
#Numbers as a string: 7-3-8-5-2

def smallest_largest(array):
    arr2 = []
    array.sort()
    arr2.append(array[0])
    arr2.append(array[len(array)-1])
    return arr2

def as_string(array):
    arr2 = map(str, array)
    return "-".join(arr2)

print(smallest_largest([1,2,6,5,4]))
print(as_string([1,2,6,5,4]))
