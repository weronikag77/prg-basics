grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
# Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). 
# Use the filter() along with an anonymous function. Sample result:

# Arithmetic mean for grades <> 2.0 is 3.85#
positive_grades = list(filter(lambda x: True if x > 2.0 else False, grades))
mean = sum(positive_grades)/len(positive_grades)

print(f"Arithmetic mean for grades <> 2.0 is {mean}")