# some_list = [Client("SomeValue, 1, "SomeOtherValue"), Client("SomeoneElse" ...
class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Client(Person):

    def __init__(self, name, email, billing_method, total_bill, availability):
        super().__init__(name, email)
        self.billing_method = billing_method
        self.total_bill = total_bill
        self.availability = availability

class Partner(Person):

    def __init__(self, name, email, bike_age, bike_manufacturer, bike_type, status):
        super().__init__(name, email)
        self.bike_age = bike_age
        self.bike_manufacturer = bike_manufacturer
        self.bike_type = bike_type
        self.status = status


clients = [
    Client("Mathias", "mathias@gmail", "per_KM", 25, "Closed"),
    Client("Peter", "peter@gmail", "per_KM", 12, "Closed"),
    Client("Paul", "paul@gmail", "per_hour", 20, "Closed"),
    Client("Mary", "Mary@gmail", "per_day", 125, "Closed"),

]


partners = [
    Partner("Jake", "jake@gmail", 12, "Trek", "Mountain", "Unavailable"),
    Partner("Alex", "alex@gmail", 4, "Merida", "Crossover", "Unavailable"),
    Partner("Ben", "ben@gmail", 8, "Kona", "Street", "Unavailable"),
    Partner("Sara", "sara@gmail", 25, "Kink", "BMX", "Available"),
]