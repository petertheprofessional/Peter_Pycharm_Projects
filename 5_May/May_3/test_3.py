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

# def get_user(username, password):
#     for user in users:
#         if user["name"] == username and user["password"] == password:
#             return user
#     return None

def get_mod(username, modulename = None):
    stash = []
    for user in username:
        if user["name"] == username:
            return user
        for mod in user.get('modules', []):
            if mod == modulename:
                stash.append(user)
    return stash


# def is_student(user):
#     return user['type'] == "Student"

# def show_registration(username, password, modulename):
#     user = get_user(username, password)
#     mod = get_mod(modulename)
#     if user is_student(user) and mod get_mod(mod):
#         print(f"You are registered to the module {modulename}")




if __name__ == '__main__':
    username = input("What is your username? ")
    # password = input(f"Type the password for username {username}: ")
    modulename = input("What module do you want to check? ")
    # user = show_registration(username, password, modulename)
    mod = get_mod(modulename)
    if mod:
        print(f"welcome, {modulename}")
    if not mod:
        print(f"Go away, {modulename}")

#print(users[2]['name'], users[2]['type'], users[2]['modules'][0]['title'])