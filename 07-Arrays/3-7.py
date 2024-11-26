#AAn array contains a list of Polish names:

arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

#Create a program that prints the longest name (consisting of the largest number of characters). 

longest = arr[0]
for i in range(0, len(arr)):
    if len(arr[i]) > len(longest):
        longest = arr[i]

print("List of names: ", *arr)
print("Longest name:", longest)
