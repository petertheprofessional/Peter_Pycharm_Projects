from dog import Dog


class GermanShepard(Dog):
    def __init__(self):
        super().__init__()

    def walk(self):
        super().walk()
        print("German Shepard`s show their beautiful fur while running.")