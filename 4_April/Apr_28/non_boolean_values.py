
username_input = input("What is your username?")
username = "admin"

welcome_message = None # Optional

if __name__ == '__main__':
    if username_input == username:
        welcome_message = "Thank you for logging in!"
    else:
        welcome_message = "Try again!"

    print(welcome_message)