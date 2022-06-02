class Fruits:
    def __init__(self):
        self.list = ['apple', 'mango', 'grapes']

    def print(self):
        print(self.list)

    def __call__(self, *args, **kwargs):
        print("Wow I cn be called now")




if __name__ == '__main__':
    a = Fruits()
    a.print()
    a()