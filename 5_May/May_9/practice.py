l1 = [2, 3, 4, 5, 8, 10]
l2 = [9, 4, 3, 9, 3, 1]
#online solve
# together = zip(l1, l2)
# sum = [x + y for (x, y) in zip(l1, l2)]
# print(sum)

# class solve
result = []
for index in range(len(l1)):
    result.append(l1[index] + l2[index])
    print(result[index])






# # for index in range(6):
#     print(l1[index])
# range only allows for a fixed number of objects

# for element in l1:
#     print(element)
#in this case it adapts to the size of the list

# for index in range(len(l1)):
#     print(l1[index]**2) #** is an exponent

