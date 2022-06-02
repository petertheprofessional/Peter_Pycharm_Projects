# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# # Your code here
# if valid["username"] == username and valid["password"] == password:
#     print(f"Welcome, {username}")
# else:
#     print("Credentials are invalid")]

###############################################
# import datetime
# def isweekend(date=datetime.datetime.now()):
#     if date.weekday() > 4:
#         return True
#     else:
#         return False
#
#
# print(isweekend(datetime.date(2021, 8, 6)))
# print(isweekend(datetime.date(2021, 8, 7)))
# print(isweekend(datetime.date(2021, 8, 8)))
# print(isweekend(datetime.date(2021, 8, 9)))]
####################################################
# import datetime
# def isweekend(date=datetime.datetime.now()):
#     if date.weekday() > 4:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     username = input("What is your username? ")
#     password = input(f"Type the password for username {username}: ")
#     valid = {"username": "admin", "password": "admin"}
#
#     today = datetime.date(2021, 8, 7)
#     today = datetime.datetime.now()
#
#     if (username == valid["username"] and password == valid["password"]) or isweekend(today):
#         print(f"Welcome, {username}")
#     else:
#         print("Credentials are invalid")
################################################
# users = [
#     {
#         "name": "Holly",
#         "password": "hunter"
#     },
#     {
#         "name": "Peter",
#         "password": "pan"
#     },
#     {
#         "name": "Janis",
#         "password": "joplin"
#     }
# ]
#
# def get_user(username, password):
#     for user in users:
#         if user["name"] == username and user["password"] == password:
#             return user
#     return None
#
#
# if __name__ == '__main__':
#     username = input("What is your username? ")
#     password = input(f"Type the password for username {username}: ")
#     user = get_user(username, password)
# if not user:
#     print("An error occurred. You are not authorized.")
##########################################################################
# users = [
#     {
#         "name": "Holly",
#         "type": "Student",
#         "password": "hunter"
#     },
#     {
#         "name": "Peter",
#         "type": "Student",
#         "password": "pan"
#     },
#     {
#         "name": "Janis",
#         "type": "Teacher",
#         "password": "joplin"
#     }
# ]
#
#
# def get_user(username, password):
#     for user in users:
#         if user["name"] == username and user["password"] == password:
#             return user
#     return None
#
# def show_offers(username, password):
#     user = get_user(username, password)
#     if not user or user['type'] == "Student":
#         print("We have great courses to offer you!")
#
# if __name__ == '__main__':
#     username = input("What is your username? ")
#     password = input(f"Type the password for username {username}: ")
#     show_offers(username, password)
users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]



def show_registration(modulename):
    find_module = None
    # for user in users:
    #     if user["name"] == username and user["password"] == password:
    #         find_module = user
    if find_module:
        for module in find_module["modules"]:
            if "title" in module == modulename:
                print(f"You are registered to the module {modulename}")
    # elif find_module:
    #     for user in users:
    #         if user["type"] == "Teacher":
    #             print("You are a Teacher")
    return modulename



if __name__ == '__main__':
    # username = input("What is your username? ")
    # password = input(f"Type the password for username {username}: ")
    # modulename = input("What module do you want to check? ")

    # print(f"What is your username? {username}")
    # print(f"What is your password? {password}")
    # print(f"What module do you want to check? {modulename}")
    show_registration("Computer basics")