from db import Bill


class SimpleBillStrategy:

    def calculate(self):
        return 100


class RentManagement:

    def __init__(self, partner_management, client_management):
        self.partner_management = partner_management
        self.client_management = client_management
        self.bills = []

    def rent(self):
        self.bicycle_list()
        option = int(input("Which Bike do you want to rent?"))
        partner = self.partner_management.partners[option]
        client_id = int(input("Please provide your client ID"))
        client = self.client_management.get_client_by_id(client_id)

        if partner.bike.status == "AVAILABLE":
            partner.bike.status = "NOT_AVAILABLE"
            bill = Bill(client, partner, SimpleBillStrategy())
            self.bills.append(bill)
            print("Done!")
        else:
            print("Bike chosen not available!")

    def return_bicycle(self):
        id = int(input("Provide your ID "))
        client = self.client_management.get_client_by_id(id)
        bill = self.find_pending_bill_by_client(client)
        if bill is not None:
            bill.total_price = bill.bill_strategy.calculate()
            bill.status = "CLOSED"
            bike = bill.partner.bike
            bike.status = "AVAILABLE"

    def find_pending_bill_by_client(self, client):
        for bill in self.bills:
            if bill.client.id == client.id:
                if bill.status == "PENDING":
                    return bill
        return None

    def bicycle_list(self):
        print('\n\n------------')
        count = 0
        for partner in self.partner_management.partners:
            bike = partner.bike
            print(f'{count}. {bike.type} - {bike.manufacturer} - {bike.year} : {bike.status}')
            count += 1
        print('------------\n\n')

    def bills_list(self):
        for bill in self.bills:
            print(f'{bill.client.name} <- {bill.partner.name} : {bill.status}')

    def report(self):
        total = 0
        for bill in self.bills:
            total += bill.total_price

        print(f"The total incoming is {total}")


class ClientManagement:

    def __init__(self, client_list):
        self.clients = client_list

    def get_client_by_id(self, client_id):
        for client in self.clients:
            if client.id == client_id:
                return client
        return None


class PartnerManagement:

    def __init__(self, partner_list):
        self.partners = partner_list