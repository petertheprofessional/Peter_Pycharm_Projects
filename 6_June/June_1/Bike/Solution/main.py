from rent import PartnerManagement
from rent import ClientManagement
from rent import RentManagement

import db


def main_menu():
    print("1. Rent a bicycle")
    print("2. Return a bicycle")
    print("3. List bicycle")
    print("4. List Bills")
    print("5. Incoming Report")
    print("0. Exit")
    opt = int(input("Type an option >> "))
    return opt


if __name__ == '__main__':

    partners_management = PartnerManagement(db.partners)
    clients_management = ClientManagement(db.clients)
    rent_management = RentManagement(partners_management, clients_management)

    option = -1
    while option != 0:

        option = main_menu()

        if option == 1:
            rent_management.rent()
        elif option == 2:
            rent_management.return_bicycle()
        elif option == 3:
            print(rent_management.bicycle_list())
        elif option == 4:
            rent_management.bills_list()
        elif option == 5:
            print(rent_management.report())