from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def print(self):
        pass

class Dog(Animal):

    def print(self):
        print("I am a dog...")

class Cat(Animal):

    def print(self):
        print("I am a cat")

class Bird(Animal):

    def output(self):
        print("I am a bird")

    def print(self):
        self.output()

if __name__ == '__main__':
    d = Dog()
    c = Cat()
    b = Bird()

    list_of_animals = [d, c, b]

    for animal in list_of_animals:
        animal.print()