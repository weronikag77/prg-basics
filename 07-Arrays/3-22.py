#Define a function rand_elem(array) that returns a randomly selected array element. 
#Using the function, print a few randomly selected array elements.
import random

arr = [1,2,3,7,8,4]

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]

print(rand_elem(arr))