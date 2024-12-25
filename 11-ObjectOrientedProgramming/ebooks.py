#1. Create a book with a title, author, number of pages 
# (check how to set the initial values of the fields at the time of 
# creating the object using the __init__ method / constructor and passing 
# the initial values as arguments to the method call)

class ebook():
    def __init__(self):
        self.title = "Lalka"
        self.author = "Bolesław Prus"
        self.pages_no = 688
        self.is_open = False
        self.page = 1
    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def next_page(self):
        if self.is_open == True and self.page > 0 and self.page < self.pages_no:
            self.page += 1
        elif self.is_open == False:
            print("Book is closed.")

    def display_status(self):
        print(f"Book title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of pages: {self.pages_no}")
        print(f"Current page number: {self.page}")
