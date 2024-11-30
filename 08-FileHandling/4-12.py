#The file books.csv contains a list of books. Write a program that copies the book data from a given genre to its corresponding file. Use functions to divide the program into logical parts.

#Genre --> Filename
#Fantasy --> books_fantasy.txt
#Historical --> books_historical.txt
#Romance --> books_romance.txt
#Classic --> books_classic.txt  

books = "books.csv"
fantasy_file = "books_fantasy.txt"

def fantasy(books, new_file):
    with open(books, "r") as file:
        with open(new_file, 'a') as file2:
            for line in file:
                if "Fantasy" in line:
                    text = file2.write(f"{line}")
            return text
            

print(fantasy(books, fantasy_file))

def historical(books, new_file):
    with open(books, "r") as file:
        with open(new_file, 'a') as file2:
            for line in file:
                if "Historical" in line:
                    text = file2.write(f"{line}")
            return text
    
history_file = "books_historical.txt"
print(historical(books, history_file))