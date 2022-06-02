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


user1.update_data("Peter", "Bautzner", "peter@gmail.com")
user1.update_data("Sara", "Sara_Street", "Sara@gmail.com")
user1.update_data("Torte", "Torte_Street", "Torte@gmail.com")
user2.name = "Sara"
user3.name = "Torte"


print(f"Name: {user1.name}, Address: {user1.address}, email: {user1.email}")
print(f"Name: {user2.name}, Address: {user2.address}, email: {user2.email}")
print(user2.name)
print(user3.name)