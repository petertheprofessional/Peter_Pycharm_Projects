# collection of "usernames"


def logged_in (x, y):
    #conditional logic
    if (x == "admin" or x == "user") and y == "123456":
        print("You have successfully logged in")
    elif (x != "admin" or x != "user") and y == "123456":
        print("Your username is incorrect")
    elif (x == "admin" or x == "user") and y != "123456":
        print("Your password is incorrect")
    else:
        print("Both username and password is incorrect")
if __name__ == '__main__':
    print("What is your username?")
    username = input()
    print("What is your password?")
    password = input()
    logged_in(username, password)