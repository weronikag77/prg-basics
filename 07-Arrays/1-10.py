#Write a program that prints information about the test results:

#Number of questions:
#Number of correct answers:
#Number of incorrect answers:
#Percentage of correct answers:
###

test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)
print(f"Number of questions: {question_number}")

# calculates the number of correct answers
sum_correct = 0
for item in test_results:
    if item == True:
        sum_correct += 1
print(f"Number of correct answers: {sum_correct}")

# calculates the number of incorrect answers
sum_incorrect = 0
for item in test_results:
    if item == False:
        sum_incorrect += 1
print(f"Number of incorrect answers: {sum_incorrect}")

# calculates the percentage of correct answers
percentage = sum_correct/len(test_results) * 100
print(f"Percentage of correct answers: {percentage}%")