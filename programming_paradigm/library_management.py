# library_management.py

class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title if available.
        Returns True if checkout succeeded, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Return a book by title.
        Returns True if return succeeded (book found), False otherwise.
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all available books, one per line in 'Title by Author' format."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            # print nothing or a message depending on your preference;
            # tests usually expect nothing when no books, but we print a friendly message:
            print("No books available.")
            return
        for book in available:
            print(f"{book.title} by {book.author}")
