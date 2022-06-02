import math


class Age:

    def __init__(self, date):
        self.date = date

    @staticmethod
    def calculate_age(date):
        print("Calculating the age...")

class Person:
    def __init__(self, name, birthday, id_number):
        self.name = name
        self.birthday = birthday
        self.id_number = id_number

    def set_name(self, name):
        self.name = name
        return name

    @staticmethod
    def calculate_age(dob):
        print("Calculating the age...")
        print(dob)

if __name__ == '__main__':
    Person.calculate_age("01.12.2022")
    Age.calculate_age("12.12.2021")

    #Person.set_name("Some Name") #wont work because it is not a static method
    p1 = Person("Someone", "May", 112)
    print(p1.set_name("Peter"))
