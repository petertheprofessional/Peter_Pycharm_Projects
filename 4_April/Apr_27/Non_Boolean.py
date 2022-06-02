password = input("What is your password")
while not password:
    print("Try again")
    password = input("What is your password")

if password == "abcd":
    print("Welcome")
else:
    print("You are wrong")