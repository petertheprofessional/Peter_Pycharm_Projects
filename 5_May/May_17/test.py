# password1 = "Peter"
# password2 = "123"
# password3 = "Peter123"
#
# if password3.isdigit():
#     print("True")
# else:
#     print("False")
#
# if password1.isalpha():
#     print("True")
# else:
#     print("False")

# users = [
#     {"password1": "Peter123"
#
#     }
# ]
#
# for user in users:
#     if user["password1"].isalpha() is True:
#         print("True")
#     else:
#         print("False")
# def load_my_file():
#     with open('list.json') as file:
#         return json.load(file)
#
# def save_to_file(data):
#     with open('list.json', mode='w') as file:
#         json.dump(data, file, indent=2)
#
if __name__ == '__main__':
    people ={"name": "Peter"}
    with open('my_output.txt', mode='w') as file:
        file.write(people)