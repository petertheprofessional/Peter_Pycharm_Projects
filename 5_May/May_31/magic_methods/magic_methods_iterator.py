class EvenNumber:

    def __init__(self, limit=100):
        self.counter = -2
        self.limit = limit


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration()

        self.counter += 2
        return self.counter



if __name__ == '__main__':

    sequence = EvenNumber(limit=10)

    for num in sequence:
        print(num)


