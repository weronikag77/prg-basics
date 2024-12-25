import ebooks

def main():
    book = ebooks.ebook()

#2. Open a book
    book.open_book()

#3. Display a book status (title, author, page numbers, current page no)
    book.display_status()

#4. Read a few pages
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()
    book.next_page()

#5. Display a book status
    book.display_status()

#6. Close a book
    book.close_book()

#7. Read a few pages (it should not be possible to perform this operation).
    book.next_page()


if __name__ =="__main__":
   main()

