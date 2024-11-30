# Then write a program that, based on the it_company.csv file, prints the first name, 
# last name and email (in the given order, without Job Title) 
# of people employed in the position of 'Graphic Designer'. Sample result:

import csv

with open("it_company.csv") as file:
    csv_read = csv.reader(file)
    print("GRAPHIC DESIGNERS:")
    print("=================")
    for line in csv_read:
        if line[2] == "Graphic Designer":
            print(f"{line[1]} {line[0]},{line[3]}")