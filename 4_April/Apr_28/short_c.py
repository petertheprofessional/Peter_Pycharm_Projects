a = 2
b = 3
def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def divide_function():
    if b > 0 and a < 100:
        return divide(a, b)

def operation_in_class():
    if divide_function() or a == 5:
        print('succesfully divided')
    else:
        return add(a, b)
        # add a print statement that tells us it was successfull
