#Measuring stations recorded the following temperatures in degrees Celsius:

dictionary = {"Krakow":7, "Warszawa":-2, "Sopot":4, "Koszalin":-1, "Opole":3}

# Write a program that displays the names of towns where positive temperatures were recorded. 
# Use anonymous and filter() functions. Sample result:

positive = list(filter(lambda x: True if dictionary[x] > 0 else False, dictionary))
# Cities with positive temperatures: Krakow Sopot Opole
print(*positive, sep=" ")