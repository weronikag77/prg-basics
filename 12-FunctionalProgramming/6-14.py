#In a beverage factory, a machine fills 500ml bottles. 
#The computer checks whether the bottle has been filled correctly. For a 500ml bottle, 
#the allowable tolerance is 2%. In the last ten bottles checked, the filling was:

ml = [508,500,512,499,492,511,503,476,501,509]

#Write a program that calculates the percentage of incorrectly filled bottles. 
#Use the filter() along with a higher order function. Sample result:

#Bottle capacity:    500ml
#Filling tolerance:  2%
#Filled bottles:     508,500,512,499,492,511,503,476,501,509
#Incorrectly filled: 30%

def is_correct(number):
    if number < 500*1.02 and number > 500*0.98:
        return True
    else:
        return False
    
bottles = list(filter(lambda x: True if is_correct(x) == True else False, ml))
incorrect = (len(ml) - len(bottles))/len(ml)

print("Bottle capacity: 500ml")
print("Filling tolerance: 2%")
print("Filled bottles:", end=" ")
print(*ml, sep = ", ")
print(f"Incorrectly filled: {incorrect*100}%")
#Incorrectly filled: 30%