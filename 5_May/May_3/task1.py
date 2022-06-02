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

def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

def show_registration (username, password, modulename):
    user = get_user(username, password)
    for leute in users:
        if leute[user["title"]] == modulename:
            print(f"You are not register to the module {modulename}:")
    if not user or not ["modules", ["title"]] == modulename:
        print(f"You are not register to the module {modulename}:")



username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)