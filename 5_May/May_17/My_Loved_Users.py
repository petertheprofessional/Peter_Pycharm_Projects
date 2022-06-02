import json

def load_users():
    with open("user.json") as file:
        return json.load(file)

def get_subscribers():
    users = load_users()
    result = []
    for user in users:
        if user["is_subscriber"] is True:
            result.append(user)
    return result

def get_active_users():
    users = load_users()
    result = []
    for user in users:
        if user["is_active"] is True:
            result.append(user)
    return result

def get_weak_passwords():
    # Mathias Solution
    # users = load_users()
    # result = []
    # for user in users:
    #     letter = False
    #     number = False
    #     for char in user['password']:
    #         if char.isalpha():
    #             letter = True
    #         elif char.isnumeric():
    #             number = True
    #     if letter is not True or number is not True:
    #         result.append(user)
    # return result
    users = load_users()
    result = []
    for user in users:
        if user["password"].isalpha() is True or user["password"].isdigit() is True:
            result.append(user)
    return result

def get_number_of_users():
    users = load_users()
    return len(users)
def login(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password and user["is_active"] is True:
            return True
def generate_contact_list():
    users = load_users()
    keys = []
    values = []
    for user in users:
        if user["name"]:
            keys.append(user["name"])
        if user["email"]:
            values.append(user["email"])
    results = dict(zip(keys, values))
    return results




if __name__ == '__main__':
    # subs = get_subscribers()
    # for sub in subs:
    #     print(sub)
    # print("-----------------------")
    # actives = get_active_users()
    # for active in actives:
    #     print(active)
    # print("-----------------------")
    # weaks = get_weak_passwords()
    # for weak in weaks:
    #     print(weak)
    # print("-----------------------")
    # users = get_number_of_users()
    # print(f"There are {users} users")
    # username = input("What is your username?")
    # password = input("What is your password?")
    # successful_login = login(username, password)
    # if successful_login is True:
    #     print("You are successfully logged in")
    # else:
    #     print("please consider subscribing")
    with open('contact_list.txt', mode='w') as file:
        json.dump(generate_contact_list(), file)



