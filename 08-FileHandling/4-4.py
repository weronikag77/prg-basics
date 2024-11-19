#Write a program that displays the first five lines from the it_company.csv file 
#and then prints 'Press Enter key...' in the next line and waits for the Enter key to be pressed. 
#The program repeats printing the next five lines from the file, waiting for the Enter key to be pressed each time.

def read_from_file(name):
    with open(name, "r") as file:
        content = file.read()
    return content

name = "it_company.csv"



