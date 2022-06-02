class Data:
    def __pow__(self, power, modulo=None):
        return (self, power, modulo)

x, y, m = Data(), Data(), Data()
print(pow(999, 888, 44))
print(pow(10, 2.1))