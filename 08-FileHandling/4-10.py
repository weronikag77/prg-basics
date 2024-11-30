# Write a program that prints those products whose 
# price is less than 60 and whose stock is less than 40.

import csv

with open("clothing.csv") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for line in csvreader:
        if float(line[5]) < 60 and int(line[6]) < 40:
            print(line)