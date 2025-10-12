import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Calculate area - must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * (self.radius ** 2)
