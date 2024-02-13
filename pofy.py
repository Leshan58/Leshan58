import math


class shape:
    def calculateArea(self):
        pass


class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
            return math.pi * (self.radius ** 2)

def calculate_total_area(shapes):
            total_area = 0
            for shape in shapes:
                total_area += shape.calculateArea()
                return total_area

mycircle= Circle(9)
myrectangle = Rectangle(5, 7)


print(f"The area of the circle is {mycircle.calculateArea()}")
print(f"The area of rectangle is {myrectangle.calculateArea()}")
