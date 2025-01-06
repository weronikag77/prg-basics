#The array below contains employee data:
import operator
arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

# Write a program that determines and displays a list of employees whose last names are given in 
# capital letters followed by first names, separated by commas. Sample result:
arr2 = []
#SMITH, Lucy
#JONES, Janet

for item in arr:
    arr2.append(list(item))

for a in arr2:
    a[0] = a[0].upper()

for item in arr2:
    print(*item, sep=", ")