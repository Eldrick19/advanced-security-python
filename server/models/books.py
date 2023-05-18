from dataclasses import dataclass

@dataclass
class Book:
    def __init__(self, title, author, year, isbn, id=None):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.id = id
    
    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, year={self.year}, isbn={self.isbn}, id={self.id})"
    
    # Function that updates the book's attributes, if an attribute isn't passed in, it will not be updated
    def update(self, title=None, author=None, year=None, isbn=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year
        if isbn:
            self.isbn = isbn

    # Get the number of letters in a book's title
    def get_title_length(self):
        return len(self.title)
    
    # Get the number of books that belong to a specific author, from a list of books
    @staticmethod
    def get_num_books_by_author(author, books):
        return len([book for book in books if book.author == author])