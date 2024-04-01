class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name} - {self.author}"


class Library:
    def __init__(self, books=[]):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, name, author):
        book = None
        for _book in self.books:
            if _book.name == name and _book.author == author:
                book = _book
                break
        return book

    def borrow_book(self, name, author):
        book = self.get_book(name, author)
        self.books.remove(book)


library = Library()
python = Book("Python", "John")
java = Book("Java", "Anji")
cbook = Book("C", "Dennis")
library.add_book(python)
library.add_book(java)
library.add_book(cbook)

# library.borrow_book("Java", "Anji")

for book in library.books:
    print(book)
