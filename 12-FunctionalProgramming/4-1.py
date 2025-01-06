#The following people are employed in one of the company's departments:

employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]

#Save the list of employees in a string array. Then, write a program that displays people 
# whose surnames start with the letter 'J'. Use anonymous and filter() functions. 

filtered = list(filter(lambda item: True if item[0] == "J" else False, employees))
print(*filtered, sep="\n")