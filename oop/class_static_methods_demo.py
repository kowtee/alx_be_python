class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Perform addition of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Perform multiplication of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
