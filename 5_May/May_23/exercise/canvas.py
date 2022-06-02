from shapes import Rectangle, Triangle
from shapes import Pentagon, Circle

class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

    def print(self):
        for shape in self.shapes:
            shape.print()