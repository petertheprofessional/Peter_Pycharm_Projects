password = input("What is your password?")
# verison 1
our_secret = "123445"
second_password = "111"
third_password = "987654"
is_correct_password = password == our_secret or second_password == password or third_password == password
if not is_correct_password:
    print("Hey, try again")
else:
    print("Thank you")

# version 2
if not is_correct_password == our_secret:
    print("Hey, try again")
else:
    print("Thank you")

# version 3
if password == our_secret:
    print("Thank you")
else:
    print("Thank you")