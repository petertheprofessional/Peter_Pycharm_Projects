class Square():

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __mul__(self, other):
        return self.area() * other.area()

    def __floordiv__(self, other): # get an int
        return self.area() // other.area()

    def __truediv__(self, other): # get a float
        return self.area() / other.area()

    def __mod__(self, other):
        return self.area() % other.area()








if __name__ == '__main__':
    square1 = Square(10)
    square2 = Square(5)

    sum_of_squares = square1 + square2
    difference = square1 - square2
    product = square1 * square2
    quotient1 = square1 // square2
    quotient2 = square1 / square2
    remainder = square1 % square2

    print(sum_of_squares)
    print(difference)
    print(product)
    print(quotient1)
    print(quotient2)
    print(remainder)