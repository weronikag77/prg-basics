def compare(arr1, arr2):
    if arr1 == arr2:
        print("Array1: ", arr1)
        print("Array2: ", arr2)
        print("arrays are the same")
    else:
        print("Array1: ", arr1)
        print("Array2: ", arr2)
        print("arrays are not the same")
    

arr1 = ["water","book"]
arr2 = ["water","book","sky"]
print(compare(arr1,arr2))