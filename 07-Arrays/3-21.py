#Write a program that checks whether the first array is a subset of the second one 
#(whether all elements of the first array appear in the second array).

arr1 = [1,2,3,8]
arr2 = [3,4,5,1,2]
arr1 = set(arr1)
arr2 = set(arr2)
print(arr1.issubset(arr2))