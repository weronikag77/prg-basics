#Students obtained the following test results (in points, from 0 to 100):

test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

print(test_results[0]["result"])

list1 = []
# Write a program that displays students whose scores are between 50 and 70 points. 
# Use an anonymous function and filter() function.
scores = list(filter(lambda x: True if x["result"] > 50 and x["result"] < 70 else False, test_results))

for i in scores:
    list1.append(i["name"])

print(list1)