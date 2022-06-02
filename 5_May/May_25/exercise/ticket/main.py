# Person1 wants to go to Berlin, trade_show, for Apple

import json
import random

def load_users():
    with open("user.json") as file:
        return json.load(file)

class Authenticator:

    def __init__(self):
        self.valid = load_users()


    def authenticate(self, user, password):
        for value in self.valid:
            if user == value["username"] and password == value["password"]:
                return True
            else:
                return False
        # TODO impliment authentication logic
        # TODO create token class


class Token(Authenticator): #token class will generate a unique id when a user is authenticated
    def __init__(self):
        super().__init__()

    def create_token(self): # create a dictionary
        list_of_tokens = []
        if super().authenticate(user, password) is True:
            n = random.randint(10000000, 99999999)
            list_of_tokens.append(n)
        return list_of_tokens






class TicketAgent:
    def __init__(self, token):
        self.token = token
    def search_flights(self, origin, destination):
        # TODO impliment search flight
        # TODO return a list of flights (flight class)
        return []
    def search_events(self, event):
        # TODO impliment search event
        # TODO return a list of events (event class)
        return []

    def search_companies(self, search_str):
        # TODO impliment search company
        # TODO return a list of companies (companyies class)
        return []


class UserManager:
    def __init__(self, token):
        self.token = token
        self.current_user = None

    def get_user(self, token):
        # TODO impliment the logic
        return None


if __name__ == '__main__':

    user = input("Type your username: ")
    password = input("Type your password: ")

    authenticator = Authenticator()
    token = authenticator.authenticate(user, password)
    n = Token.create_token()
    print(n)


    # ticket_agent = TicketAgent(token)
    # user_manager = UserManager(token)
    #
    # print("1 Search for flight tickets...")
    # print("2 Search for event tickets...")
    # print("3 Find companies...")
    # print("4 Manage Your Account")
    # option = int(input(">>"))
    #
    # if option == 1:
    #     origin = input("Where From? ")
    #     destination = input("Where To? ")
    #     list_of_flights = ticket_agent.search_flights(origin, destination)
    #     print(list_of_flights)
    # elif option == 2:
    #     event = input("Type the event name: ")
    #     list_of_tickets = ticket_agent.search_events(event)
    # elif option == 3:
    #     search_str = input("Type a text to search for companies: ")
    #     companies = ticket_agent.search_companies()
    # elif option == 4:
    #     user_manager.current_user.set_name("Peter")
    #     user = user_manager.get_user(token)
    #     print(user)
