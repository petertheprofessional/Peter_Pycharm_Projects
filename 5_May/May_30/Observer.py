from abc import ABC, abstractmethod

class Observable(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass


class Observer(ABC):

    @abstractmethod
    def notify(self):
        pass

class SmokeSensor(Observable):

    def __init__(self):
        self.list_observers = []

    def attach(self, observer):
        self.list_observers.append(observer)

    def detach(self, observer):
        self.list_observers.remove(observer)

    def smoke_dectected(self):
        for observer in self.list_observers:
            observer.notify()

class Firefighter(Observer):

    def notify(self):
        print("Something is creating smoke")

class Police(Observer):

    def notify(self):
        print("Who started to fire")

class Victims(Observer):

    def notify(self):
        print("Help us we are Panicking!")

if __name__ == '__main__':

    smoke_sensor =SmokeSensor()
    police_dep = Police()
    smoke_sensor.attach(police_dep)
    firefighters = Firefighter()
    smoke_sensor.attach(firefighters)

    victims = list()

    for i in range(5):
        victims = Victims()
        smoke_sensor.attach(victims)

    smoke_sensor.smoke_dectected()