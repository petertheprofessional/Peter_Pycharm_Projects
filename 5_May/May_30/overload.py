class Ticket:

    def find_ticket(selfs, x, y, z): #conditional arguments
        print(f"hallo {x} {y} {z}")

    def find_ticket2(self, name, maximum=None, minimum=None): #overloading arguments
        if maximum == None and minimum == None:
            print(f" hi {name}")
        elif maximum is not None:
            print(f" hi {name} -> Maximum {maximum}")

    def find_ticket3(self, name, **kwargs): #using kwargs
        self.name = name
        print(kwargs['maximum'])
        print(kwargs['minimum'])
        print(kwargs['avg'])
        print(self.name)
if __name__ == '__main__':
    t = Ticket()
    t.find_ticket(1, 2, 3)
    t.find_ticket2("Peter", 1000)
    t.find_ticket2("jake") #follows the logic and doesnt require the two arguments that arent used
    t.find_ticket3("Bob", maximum=1000, minimum=0, avg=500)