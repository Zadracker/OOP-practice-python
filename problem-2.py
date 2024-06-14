# Challenge: Create an abstract class Shape with an abstract method area, and implement it in subclasses like Circle and Rectangle.

from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Subclass Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(3, 4)

# Calculating and printing areas
print("Area of the circle:", circle.area())
print("Area of the rectangle:", rectangle.area())
