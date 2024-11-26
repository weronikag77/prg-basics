#Write a program that converts any natural number to a binary number. Use the stack. To convert a number, divide the number by 2, 
#each time taking the remainder of the division and putting the remainder on the stack. 
#Repeat the division until the number you are dividing is zero.

import queue
binary_number = queue.LifoQueue()

number = 18

while number > 0:
    n = number%2
    binary_number.put(n)
    number = number//2

while not binary_number.empty():
    bin = binary_number.get()
    print(bin, end="")


