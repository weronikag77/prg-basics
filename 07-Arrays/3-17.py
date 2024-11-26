#Write a program that counts the number of occurrences of any value from a tuple. Sample result:

#Tuple: 50,20,40,50,30,50
#Value: 50
#Number of occurrences: 3

tuple = (50,20,40,50,30,50)

number = 50
occurrences = tuple.count(number)
print("Tuple:", end=" ")
print(*tuple, sep=",")
print("Value:", number)
print("Number of occurrences:", occurrences)
