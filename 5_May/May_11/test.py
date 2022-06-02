# class_list = dict()
#
# key = input("Key")
# value = input("Value")
# class_list[key] = value
# print(class_list)


# lis = []
#
# for x in range(2):
#     lis.append(input("Input: "))
#
# print(lis)

key_list = [{
    "Dimensions": {
      "Height": 140,
      "Length": 143,
      "Width": 202
    }}]
for key in key_list:
    key['Dimensions']['Width'] = 120
print(key_list)

