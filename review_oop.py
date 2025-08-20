# This is for OOP 1.1 - Review of OOP

class Book:
        def __init__(self, title, author, pages):
                self.title = title
                self.author = author
                self.pages = pages
        def display_details(self):
                print("Title: " + self.title + ", " "Author: " + self.author + ", " "Pages: " + str(self.pages))
        def is_long_book(self):
                if self.pages > 100:
                        pages = True
                        print("Is long book: True")
                else:
                        pages = False
                        print("Is long book: False")

book1 = Book(title="The Fellowship of the Ring", author="J.R. Tolkein", pages=550)
book2 = Book(title="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling", pages=223)
book3 = Book(title="Eragon", author="Christopher Paolini", pages=100) # I know its not 100 pages, was testing False statement

book1.display_details()
book1.is_long_book() 

book2.display_details()
book2.is_long_book() 

book3.display_details()
book3.is_long_book() 