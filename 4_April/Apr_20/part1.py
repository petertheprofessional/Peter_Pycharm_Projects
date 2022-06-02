def largest_among_two(a, b):
    if a > b:
        print("a is greater than b")
    elif a < b:
        print("b is greater than a")
    else:
        print("they are the same number")
if  __name__ == '__main__':
    first = int(input())
    second = int(input())
    largest_among_two(first, second)