import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        return area

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = (self.radius ** 2)* math.pi
        return area