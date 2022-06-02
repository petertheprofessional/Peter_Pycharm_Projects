if __name__ == '__main__':
    # Task 1
    # file = open('task1.txt')
    # print(file.read())
    # file.close()
    # or
    # with open("task1.txt") as file:
    #     print(file.read())
    #######################################
    # Task 2
    # count = 0
    # with open('task2.txt') as file:
    #     lines = list(file)
    #     print(len(lines[2:]))
    # or
    # with open('task2.txt') as file:
    #     lines = list(file)
    #     print(len(lines) - 2)
    ########################################
    # Task 3

    # with open("task3.txt") as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line, end='') #original
    #     print('\n---------------------')
    #     odds = lines[::2]
    #     even = lines[1::2]
    #     for line in odds:
    #         print(line, end='')
    #     for line in even:
    #         print(line, end='')
    #or
    # with open("task3.txt") as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line, end='')  # original
    #     print('\n---------------------')
    #     for index in range(len(lines)):
    #         if index % 2 == 0:
    #             print(lines[index], end='')
    #     for index in range(len(lines)):
    #         if index % 2 == 1:
    #             print(lines[index], end='')
    ################################################
    # with open('task4.txt') as file:
    #     content = file.read()
    #     print(content[1622:1635])
    ################################################
    # Task 5
    # with open('task5.txt') as file:
    #     line = file.readline()
    #     print(line)
    #     counter = 0
    #     for char in line:
    #         if char != '\n':
    #             counter += 1
    #     print(counter)
    # or
    with open('task5.txt') as file:
        line = file.readline().strip()
        counter = 0
        for char in line:
            counter += 1
        print(counter)
    #################################################
    # Task 6
    # result = []
    # with open('task6.txt') as file:
    #     for line in file:
    #         counter = 0
    #         for char in line:
    #             counter += 1
    #         result.append(counter)
    #     print(result)

