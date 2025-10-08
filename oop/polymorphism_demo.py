import math
class Shape:
    """Base class for all shapes"""
    
    def area(self):
        """Must be implemented before subclasses"""
        raise NotImplementedError("Subclasses must override this method.")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides Shape.area()"""
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Overrides Shape.area()"""
        return self.radius * self.radius * math.pi