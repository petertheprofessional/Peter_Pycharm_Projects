class User:

    def __init__(self):
        self.name = None
        self.address = None
        self.email = None
        self.password = None

    def update_data(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

user1 = User()
user2 = User()
user3 = User()

list_of_users = [user1, user2, user3]

user1.update_data("Peter", "Bautzner", "peter@gmail.com")
user2.update_data("Sara", "Sara_Street", "Sara@gmail.com")
user3.update_data("Torte", "Torte_Street", "Torte@gmail.com")


for user in list_of_users:
    print(f"Name: {user.name}, Address: {user.address}, email: {user.email}")