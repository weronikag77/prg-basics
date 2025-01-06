#Write a program that calculates the sum of even numbers. Use filter(), reduce() and anonymous functions.
from functools import reduce
#Tip. First, use filtering to extract even numbers. Then use reduce() to calculate the sum of those numbers.

numbers = [2,4,6,3,7,5]

even_numbers = list(filter(lambda x: True if x %2 == 0 else False, numbers))
sum_even = reduce(lambda x,y: x+y, even_numbers)
print(sum_even)