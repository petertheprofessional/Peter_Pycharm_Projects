def f(**kwargs): #kwargs need a dictionary
    for key, value in kwargs.items():
        print(f"The key is {key}, the value for this key is {value}")

    print(kwargs.get("something", 100)) #100 is a default value
    print(kwargs.get("size", 100)) #returns the number of times this key is used




def e(*args): #args need a list
    total = 0
    for arg in args:
        total += arg
    return total

def g(x, y, z): #set difinitive values
    return x + y + z

if __name__ == '__main__':
    f(size=1, weight=3, age=4)
    print(e(1, 2, 3, 4, 8))
    print(g(1 ,2 , 3))