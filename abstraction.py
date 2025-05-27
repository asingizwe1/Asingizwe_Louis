#import ABC and abstractmethod from abc module
from abc import ABC, abstractmethod#abstraction
# Create an abstract class named Shape
class Shape(ABC):
    # Define an abstract method named area
    @abstractmethod
    def area(self):
        pass#this method start has no implementation

#child class can implement abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

        #we cant create objsct of abstract class
