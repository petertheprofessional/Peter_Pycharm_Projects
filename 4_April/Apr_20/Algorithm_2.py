def x(a, b, c):
    if a > b:
        if a > c:
            return print('a is the largest')
        else:
            return print('c is the largest')
    elif a < b:
        if b > c:
            return print('b is the largest')
        else:
            return print('c is the largest')
    else:
        return print('something is equal')

if  __name__ == '__main__':
    print(x(15, 12, 2))