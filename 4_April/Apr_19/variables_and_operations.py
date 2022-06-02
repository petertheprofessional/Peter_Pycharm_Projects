def f(a, b):
    return (a + b + 3)/2
def g(x, y):
    return (x + y) * x
if __name__ == '__main__':
    a = 2
    b = 3
    c = a + b
    c = (a + b + 3) / 2
    print(c)
    c = f(a, b)
    print(c)
    d = g(a, b)
    print(d)