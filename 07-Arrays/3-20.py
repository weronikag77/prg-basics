#Write a program to separate even and odd numbers of a given array of integers. 
#Put all even numbers first, and then odd numbers.

#Sample result:

#arr = [7,9,2,4,5,6]
#arr = [2,4,6,7,9,5]

arr = [7,9,2,4,5,6]
arr2 = []
arr3 = []

for item in arr:
    if item%2 == 0:
        arr2.append(item)
    else:
        arr3.append(item)
arr2 += arr3

print(arr2)
