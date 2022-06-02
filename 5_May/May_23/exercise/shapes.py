import math

class Shape:

    def __init__(self):
        self.name = ""

    def get_print(self):
        print(f"Shape is: {self.name}, its area is {self.get_area()} and its perimeter is {self.get_perimeter()}")


class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.name = "Rectangle"
        self.width = float(width)
        self.length = float(length)

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def print(self):
        super().get_print()


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.name = "Triangle"
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)


    def check_sides(self):
        if self.side1 + self.side2 > self.side3:
            if self.side1 + self.side3 > self.side2:
                if self.side2 + self.side3 > self.side1:
                    if self.side3 > abs(self.side1 - self.side2):
                        return True
        return False
    def get_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2) * (semi_perimeter - self.side3))
        return area

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def print(self):
        super().get_print()




class Pentagon(Shape):
    def __init__(self, side):
        super().__init__()
        self.name = "Pentagon"
        self.side = float(side)

    def get_area(self):
        return (1/4) * (math.sqrt( 5 * ( 5 + (2 * math.sqrt(5)))) * self.side**2)

    def get_perimeter(self):
        return self.side * 5

    def print(self):
        super().get_print()




class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = float(radius)

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def print(self):
        super().get_print()




