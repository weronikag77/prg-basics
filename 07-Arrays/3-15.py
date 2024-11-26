#Write a program that prints the tuple (10,20,30,40,50) in reverse order. Sample result:

#Tuple: 10,20,30,40,50
#Reverse order: 50,40,30,20,10

tuple = (10,20,30,40,50)
list = []

i = len(tuple)
for item in tuple:
    list.append(tuple[i-1])
    i -= 1


print(f'Tuple: ',end=" ")
print(*tuple, sep=",")
print("Reverse order: ", end=' ')
print(*list, sep=',')
