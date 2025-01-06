#The educational course finished with a test checking the participants' knowledge. 
# Here are the results obtained by the students:

array = [37,51,44,23,78,92,39,84,83,51]

#Write a program that calculates and displays student scores that are equal to or greater than the 
# following minimum number of points to pass the course:

#1. 70
#2. 40
#3. 30

#Use the filter() function and the following higher order function:

def min_pts(limit):
   return lambda pts: pts>=limit

results = list(filter(lambda x: True if min_pts(10, x) == True else False, array))

print(results)



   
