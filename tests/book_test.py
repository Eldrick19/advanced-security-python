import unittest

from server.models.books import Book

class BookTest(unittest.TestCase):
    def test_book_init(self):
        book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "0-395-07122-4")
        self.assertEqual(book.title, "The Hobbit")
        self.assertEqual(book.author, "J.R.R. Tolkien")
        self.assertEqual(book.year, 1937)
        self.assertEqual(book.isbn, "0-395-07122-4")
        self.assertEqual(book.id, None)
    
    def test_book_repr(self):
        book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "0-395-07122-4")
        self.assertEqual(str(book), "Book(title=The Hobbit, author=J.R.R. Tolkien, year=1937, isbn=0-395-07122-4, id=None)")
    
    def test_book_update(self):
        book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "0-395-07122-4")
        book.update(title="The Lord of the Rings", author="J.R.R. Tolkien", year=1954, isbn="0-395-07123-2")
        self.assertEqual(book.title, "The Lord of the Rings")
        self.assertEqual(book.author, "J.R.R. Tolkien")
        self.assertEqual(book.year, 1954)
        self.assertEqual(book.isbn, "0-395-07123-2")
    
    def test_book_get_title_length(self):
        book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "0-395-07122-4")
        self.assertEqual(book.get_title_length(), 9)
    
    def test_book_get_num_books_by_author(self):
        books = [
            Book("The Hobbit", "J.R.R. Tolkien", 1937, "0-395-07122-4"),
            Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "0-395-07123-2"),
            Book("The Silmarillion", "J.R.R. Tolkien", 1977, "0-395-07124-0"),
            Book("The Hobbit", "J.R.R. Tolkien", 1937, "0-395-07122-4"),
            Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "0-395-07123-2")
        ]