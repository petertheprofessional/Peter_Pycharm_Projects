if __name__ == '__main__':
    # task 1
    # with open("task1.txt") as file:
    #     content = file.read()
    #     print(content)

    ########################################
    # Task 2
    # count = 0
    # with open('task2.txt') as file:
    #     lines = file.readlines()[1:]
    #     for line in lines:
    #         if line.strip():
    #             count += 1
    # print(count)
    ##########################################
    # Task 3
    # with open("task3.txt") as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line, end='') #original
    #     print('\n---------------------')
    #     for index in range(len(lines)):
    #         if index % 2 == 0:
    #             print(lines[index], end='')
    #     for index in range(len(lines)):
    #         if index % 2 == 1:
    #             print(lines[index], end='')

    ###########################################
    # Task 4
    # with open('task4.txt') as file:
    #     content = file.read()
    #     print(content[1622:1635])
    ################################################
    # Task 5
    # with open('task5.txt') as file:
    #     first_line = file.readline()
    #     print(first_line)
    #     number_of_characters = 0
    #     for f in first_line:
    #         f = f.strip("\n")
    #         number_of_characters += len(f)
    #     print(number_of_characters)
    #################################################
    # Task 6
    with open('task6.txt') as file:
        number_of_characters = []
        for f in file.readlines():
            number_of_characters.append(len(f))

        print(number_of_characters)











