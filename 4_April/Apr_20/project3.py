def is_first_greater(x, y):
    if x > y:
        return True
    else:
        return False
def is_second_greater(x, y):
    return x > y

if  __name__ == '__main__':
    print(is_first_greater(3, 4))
    print(is_first_greater(9, 7))
    print("------- ")
    print(is_second_greater(3, 4))
    print(is_second_greater(8, 5))
    a = int(input())
    b = int(input())
    print(is_first_greater(a, b))