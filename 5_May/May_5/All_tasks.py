option = -1

while option < 1 or option > 3:
    print("Please select an option >>> ", end='')
    option = int(input())

###############################################

# print("What is the first number ", end='')
# a = int(input())
# print("What is the second number ", end='')
# b = int(input())
# print("What is the third number ", end='')
# c = int(input())
#
# d = a + b + c
# print(f'First number: {a}')
# print(f'Second number: {b}')
# print(f'Third number: {c}')
# print(f'The triple sum is: {d}')

##########################################

# print("What is the first number ", end='')
# a = int(input())
# print("What is the second number ", end='')
# b = int(input())
#
# if a > b:
#     c = (a - b) * 2
# else:
#     c = abs(a - b)
# print(f'First number: {a}')
# print(f'Second number: {b}')
# print(f'The result of the calculation is: {c}')

#############################################

# print("What is the number ", end='')
# a = int(input())
# if (a % 2) == 0:
#     print(f"{a} is an even number!")
# else:
#     print(f"{a} is an odd number!")

################################################
#
# import math
# print("What is the number ", end='')
# r = float(input())
# A = math.pi * (r * r)
# print(f"The Area of the circle with radius {r} is:", f"{A:.2f}")

################################################

# guess = -1
# correct_answer = 7
#
# while guess:
#     print("Guess a number between 1 and 10 until you get it right : ", end='')
#     guess = int(input())
#     if guess == correct_answer:
#         print("Well guessed!")

################################################

# def menu():
#     print('1 - Fahrenheit')
#     print('2 - Celsius')
#     print("Input the scale you'd like to convert: ", end='')
#     option = int(input())
#     return option
#
# if __name__ == '__main__':
#     choice = menu()
#     if choice == 1:
#         print("What is the temperature in Fahrenheit ", end='')
#         F = int(input())
#         C = (F-32) * 5/9
#         print(f"The temperature in Celsious is {C} degrees")
#     elif choice == 2:
#         print("What is the temperature in Celsius ", end='')
#         C = int(input())
#         F = (C * (9/5)) + 32
#         print(f"The temperature in Fahrenheit is {F} degrees")

#############################################################

# print('* ' '\n* * \n* * * \n* * * * \n')
# n = 5
#
# for x in range(n):
#     for y in range(x):
#         print('* ', end='')
#     print('')
# for x in range(n,0,-1):
#     for y in range(x):
#         print('* ', end='')
#     print('')

################################################################
# i = 0
# a = 0
# b = 1
# while i < 10:
#     if(i <= 1):
#         c = i
#     else:
#         c = a + b
#         a = b
#         b = c
#     print(c)
#     i= i + 1

# x = 0
# y = 1
#
# for z in range(0, 10):
#     if(z <= 1):
#         Next = z
#     else:
#         Next = x + y
#         x = y
#         y = Next
#     print(Next)




