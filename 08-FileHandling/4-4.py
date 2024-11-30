#Write a program that displays the first five lines from the it_company.csv file 
#and then prints 'Press Enter key...' in the next line and waits for the Enter key to be pressed. 
#The program repeats printing the next five lines from the file, waiting for the Enter key to be pressed each time.
filename = "it_company.csv"

head = ""
with open(filename) as file:
    for i in range(5):
        head+= next(file)
    print(head)
    enter = input("Press 'Enter' to continue: ")
    if enter == "":
        for i in range(5):
            head+= next(file)
        print(head)





