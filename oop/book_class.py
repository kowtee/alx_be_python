class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor that initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for users (informal)."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation (developer-friendly)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
