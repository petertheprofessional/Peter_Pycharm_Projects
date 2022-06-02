import db
from db import Client
from db import Partner

class ClientManagement:

    def __init__(self):
        self.list_of_clients = db.clients

    def get_all_clients(self):
        return self.list_of_clients

    def print(self):
        for client in self.list_of_clients:
            print(client.name, client.email, client.billing_method, client.total_bill, client.availability)

    def income(self):
        total = 0
        for client in self.list_of_clients:
            total = total + client.total_bill
        print(f"Our store income this month is ${total}")

class PartnerManagement:

    def __init__(self):
        self.list_of_partners = db.partners

    def get_all_partners(self):
        return self.list_of_partners

    def print(self):
        for partner in self.list_of_partners:
            print(partner.bike_manufacturer, partner.bike_type)

class RentManagement():

    def __init__(self):
        pass

    def rent(self):
        bike_selection = Bike()
        return bike_selection.bike_selection()


    def return_bycicle(self):
        pass

    def bycicles_list(self):
        partner = PartnerManagement()
        return partner.print()

    def bills_list(self):
        client = ClientManagement()
        return client.print()

    def report(self):
        client = ClientManagement()
        return client.income()

class Bike:

    def __init__(self):
        pass
        self.partner = PartnerManagement()

    def bike_selection(self):

        print("1. By Age")
        print("2. By Type of Bike")
        print("3. By Manufacturer of Bike")
        option = int(input(f"How would you like to look for bikes?\n"))

        if option == 1:
            Bike.bike_age(self)
        elif option == 2:
            Bike.bike_type(self)
        elif option == 3:
            Bike.bike_manufacturer(self)

    def bike_age(self):

        print("1. Less than 5 years")
        print("2. 5-10 years")
        print("3. 10-20 years")
        print("4. More than 20 years")
        option = int(input(f"How old do you mind the bike being?\n"))

        if option == 1:
            for age in self.partner.list_of_partners:
                if age.bike_age < 5:
                    print(age.name, age.email, age.bike_age, age.bike_type, age.bike_manufacturer)
        elif option == 2:
            for age in self.partner.list_of_partners:
                if age.bike_age <= 10:
                    print(age.name, age.email, age.bike_age, age.bike_type, age.bike_manufacturer)
        elif option == 3:
            for age in self.partner.list_of_partners:
                if age.bike_age <= 20:
                    print(age.name, age.email, age.bike_age, age.bike_type, age.bike_manufacturer)
        elif option == 4:
            for age in self.partner.list_of_partners:
                if age.bike_age > 20:
                    print(age.name, age.email, age.bike_age, age.bike_type, age.bike_manufacturer)

    def bike_type(self):

        print("1. Mountain")
        print("2. Crossover")
        print("3. Street")
        print("4. BMX")
        option = int(input(f"What type of bike would you like to rent?\n"))

        if option == 1:
            for type in self.partner.list_of_partners:
                if type.bike_type == "Mountain":
                    print(type.name, type.email, type.bike_age, type.bike_type, type.bike_manufacturer)
        elif option == 2:
            for type in self.partner.list_of_partners:
                if type.bike_type == "Crossover":
                    print(type.name, type.email, type.bike_age, type.bike_type, type.bike_manufacturer)
        elif option == 3:
            for type in self.partner.list_of_partners:
                if type.bike_type == "Street":
                    print(type.name, type.email, type.bike_age, type.bike_type, type.bike_manufacturer)
        elif option == 4:
            for type in self.partner.list_of_partners:
                if type.bike_type == "BMX":
                    print(type.name, type.email, type.bike_age, type.bike_type, type.bike_manufacturer)

    def bike_manufacturer(self):

        print("1. Trek")
        print("2. Merida")
        print("3. Kona")
        print("4. Kink")
        option = int(input(f"What manufacturer of bike would you like to rent?\n"))

        if option == 1:
            for man in self.partner.list_of_partners:
                if man.bike_type == "Trek":
                    print(man.name, man.email, man.bike_age, man.bike_type, man.bike_manufacturer)
        elif option == 2:
            for man in self.partner.list_of_partners:
                if man.bike_type == "Merida":
                    print(man.name, man.email, man.bike_age, man.bike_type, man.bike_manufacturer)
        elif option == 3:
            for man in self.partner.list_of_partners:
                if man.bike_type == "Kona":
                    print(man.name, man.email, man.bike_age, man.bike_type, man.bike_manufacturer)
        elif option == 4:
            for man in self.partner.list_of_partners:
                if man.bike_type == "Kink":
                    print(man.name, man.email, man.bike_age, man.bike_type, man.bike_manufacturer)




class Bill:

    def __init__(self):

        self.status = None
        self.partner = None
        self.client = None
        self.bike = None
        self.billing_method = None
        self.date = None
        self.id = None
        self.price = None

    def billing_method(self):

        choice = int(input(f"What method would you like to use to pay?\n"))
        print("1. per_KM - $0.50")
        print("2. per_hour - $5.00")
        print("3. per_day - $25.00")
        if choice == 1:
            return lambda a: a * 0.50
        elif choice == 2:
            return lambda b: b * 5
        elif choice == 3:
            return lambda c: c * 25