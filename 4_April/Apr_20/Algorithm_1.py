def x():
    print("What is the first number")
    a = input ()
    check = int(a)
    return a
def y():
    print("What is the second number")
    b = input ()
    check = int(b)
    return b

if  __name__ == '__main__':
    x = x()
    y = y()
    if x > y:
        print('The first is the larger number')
    elif x < y:
        print('The second is the larger number')
    else:
        print('they are the same number')


