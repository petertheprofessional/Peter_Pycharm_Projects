# int_l1 = list() #can only work with integers
# l1 = [1, "Peter", 3.4, True] #can have numbers or strings

class Dog:

    def print(self):
        print("I am a dog...")

class Cat:

    def print(self):
        print("I am a cat")

class Bird:

    def output(self):
        print("I am a bird")

if __name__ == '__main__':
    d = Dog()
    c = Cat()
    b = Bird()

    list_of_animals = [d, c, b]

    for animal in list_of_animals:
        animal.print()

