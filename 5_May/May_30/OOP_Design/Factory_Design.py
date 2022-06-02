from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta): # if its an interface start with I

    @abstractstaticmethod
    def person_method():
        """Interface Method""" #mentioning that each person uses the methods

class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Teacher Name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory: #This is a factory pattern

    @abstractstaticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

if __name__ == '__main__':
    choice = input("What type of person do you want to create\n")
    person = PersonFactory.build_person(choice)
    person.person_method()
