# A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard, calculates and displays the value True if the tree can be cut down, or display the value False otherwise. 
diameter = int(input('Enter the diameter (in cm): '))
cut_down = diameter >= 50
print(f'Tree can be cut down: {cut_down}')