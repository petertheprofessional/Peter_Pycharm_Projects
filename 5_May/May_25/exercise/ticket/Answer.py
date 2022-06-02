import db
import uuid
import datetime

class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

class Ticket:

    def __init__(self, price, issued_by):
        self.id = uuid.uuid4()
        self.price = price
        self.issued_by = issued_by

class FlightTicket(Ticket):

    def __init__(self, origin, destination, price, issued_by):
        super().__init__(price, issued_by)
        self.origin = origin
        self.destination = destination


    def __str__(self):
        return f'{self.origin}--->{self.destination}:{self.price}:{self.issued_by}-{self.id}'

    def __repr__(self):
        return f'{self.origin}--->{self.destination}:{self.price}:{self.issued_by}-{self.id}'

class EventTicket(Ticket):

    def __init__(self, name, address, price, issued_by):
        super().__init__(price, issued_by)
        self.name = name
        self.address = address

class CompanyName(Ticket):

    def __init__(self, company, origin, price, issued_by):
        super().__init__(price, issued_by)
        self.company = company
        self.origin = origin


class Token:

    def __init__(self, user):
        self.token = uuid.uuid4()
        self.user = user
        self.issued_on = datetime.datetime.now()
        self.valid_for = 6 # in hours



class UserController:

    def __init__(self):
        self.list_of_users = self.load_users()

    def get_user(self, username):
        for user in self.list_of_users:
            if user.username == username:
                return user
            raise Exception("User Not Found")

    def load_users(self):
        list_of_users_obj = []
        for user in db.users:
            new_user = User(user["name"], user["username"], user["password"])
            list_of_users_obj.append(new_user)
        return list_of_users_obj


class Authenticator:

    def __init__(self):
        self.list_of_tokens = {}
        self.user_controller = UserController()

    def authenticate(self, username, password):
        user = self.user_controller.get_user(username)
        if user.password == password:
            token = Token(user)
            self.list_of_tokens[user.username] = token
            return token
        else:
            raise Exception("Authentication Failed")




class TicketAgent:
    def __init__(self, token):
        self.token = token
        self.flight_tickets = self.load_flight_tickets()
        self.event_tickets = self.load_event_tickets()
        self.companies = self.load_companies()

    def search_flights(self, origin, destination):
        results = []
        for ticket in self.flight_tickets:
            if ticket.origin == origin and ticket.destination == destination:
                results.append(ticket)
        return []

    def search_events(self, event):
        results = []
        for ticket in self.event_tickets:
            if ticket.name == event:
                results.append(ticket)
        return []

    def search_companies(self, search_str):
        results = []
        for company in self.companies:
            if company.company == search_str:
                results.append(company)
        return []

    def load_flight_tickets(self):
        flights = []
        for flight_ticket in db.flight_tickets:
            flight = FlightTicket(flight_ticket["origin"], flight_ticket["destination"], flight_ticket["price"], flight_ticket["issued_by"])
            flights.append(flight)
        return flights
    def load_event_tickets(self):
        event_tickets = []
        for event_ticket in db.event_tickets:
            event_ticket = EventTicket(event_ticket["name"], event_ticket["address"], event_ticket["price"], event_ticket["issued_by"])
            event_tickets.append(event_ticket)
        return event_tickets

    def load_companies(self):
        company_names = []
        for company in db.companies:
            company_name = CompanyName(company["company"], company["origin"], company["price"], company["issued_by"])
            company_names.append(company_name)
        return company_names


class AccountManager:

    def __init__(self, token):
        self.token = token
        self.current_user = None


    def get_user(self, token):
        # TODO implement the logic
        return None


if __name__ == '__main__':

    user = input("Type your username: ")
    password = input("Type your password: ")

    authenticator = Authenticator()
    token = authenticator.authenticate(user, password)

    ticket_agent = TicketAgent(token)
    account_manager = AccountManager(token)
    print(f"Authenticated with Token {token}")

    print("1. Search for flight tickets...")
    print("2. Search for event tickets...")
    print("3. Find companies...")
    print("4. Manage Your Account")
    option = int(input(">>"))

    if option == 1:
        origin = input("From where? ")
        destination = input("destination... ")
        list_of_flights = ticket_agent.search_flights(origin, destination)
        print(list_of_flights)
    elif option == 2:
        event = input("Type the event name: ")
        list_of_tickets = ticket_agent.search_events(event)
        print(list_of_tickets)
    elif option == 3:
        search_str = input("Type a text to search for companies: ")
        companies = ticket_agent.search_companies(search_str)
    elif option == 4:
        account_manager.current_user.set_name("Mathias")
        user_account = account_manager.get_user(token)
        print(user_account)
        