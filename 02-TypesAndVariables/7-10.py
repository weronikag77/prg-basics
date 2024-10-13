#Write a program that enables a user to challenge a computer. 
# The computer throws dice. 
# Then, the user then tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. 
# If the user has guessed the number from the dice, the computer displays True. Otherwise, the computer displays False.
import random
#computer's turn
computer_guess = random.randint(1,6)
#user's turn
user_guess = int(input('Enter a number: '))
correct_guess = user_guess == computer_guess
print(correct_guess)

