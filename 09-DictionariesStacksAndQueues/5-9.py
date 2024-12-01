# A traffic camera records passing vehicles. 
# The camera saves their registration numbers in the file vehicle.txt. 
# Write a program that calculates and prints how many registered cars come 
# from each province of Poland. The list of provinces and the corresponding first letters 
# of the vehicle registration numbers are contained in the file province.csv.

# Hint: use the dictionary containing the letters corresponding to the provinces and 
# the numbers of vehicles whose first letters of the registration number match the letters 
# of the province.
import csv

dictionary = {

}

with open("province.csv", encoding="utf8") as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

print(data)

with open("vehicle.txt", encoding="utf8") as file2:
    for line in file2:
        for key, item in data.items():
            if line[0] == data[key]:
                dictionary[key] = 