class Rectangle:

    def __init__(self):
        self.width = 1
        self.height = 1

    def increase_height(self):
        self.height += 1

if __name__ == '__main__':
    print("Our program is running...")

    rec1 = Rectangle()
    rec2 = Rectangle()
    rec3 = Rectangle()

    print(rec1.height)
    print(rec2.height)
    print(rec3.height)

    rec1.increase_height()
    rec1.increase_height()

    print(rec1.height)
    print(rec2.height)
    print(rec3.height)

