class Book:
    """Represents a single book"""
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute
        self.__is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if available"""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned"""
        self.__is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out"""
        return not self.__is_checked_out


class Library:
    """Manages a collection of Book instances"""
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        """Adds a Book instance to the library"""
        if isinstance(book, Book):
            self.__books.append(book)

    def check_out_book(self, title):
        """Find and check out a book if available"""
        for book in self.__books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return False

    def return_book(self, title):
        """Find and return a book"""
        for book in self.__books:
            if book.title.lower() == title.lower():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all books that are available"""
        for book in self.__books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
