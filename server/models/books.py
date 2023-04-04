
from dataclasses import dataclass

@dataclass
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def turn_page(self, forward=True):
        if forward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, currently on page {self.current_page}"
    
    def get_author(self):
        return self.author

