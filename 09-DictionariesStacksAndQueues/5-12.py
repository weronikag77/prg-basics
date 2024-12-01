# Define a function that takes a string as input and uses a stack to reverse it. 
# Then, write a program to reverse any text entered from the keyboard.

# Hint: Push each character of the string onto the stack, then pop characters to form the reversed string.
import queue

word = input("Enter a word: ")
letters = queue.LifoQueue()

for char in word:
    letters.put(char)

string = ""
for i in range(len(word)):
    letter = letters.get()
    string += letter

print(string)