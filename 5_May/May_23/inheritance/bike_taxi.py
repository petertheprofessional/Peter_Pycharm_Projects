from vehicle import Vehicle
from bike import Bike
from public_transport import PublicTransport

class BikeTaxi(Bike, PublicTransport):
    def __init__(self, motorized, **kwargs):
        super().__init__(**kwargs)
        self.motorized = motorized
        if self.motorized:
            self.max_passengers = 4
            self.speed = 30
        else:
            self.max_passengers = 2
            self.speed = 18
        super().__init__(speed=self.speed, motorized=self.motorized)

    def enter_passengers(self, num: int):
        allowed_number = self.max_passengers - self.get_current_passengers()
        if self.get_current_passengers() > self.max_passengers:
            print(f"Cannot load more passengers")
        elif self.get_current_passengers() + num > self.max_passengers:
            print(f"Cannot load more passengers, only {allowed_number}.")
        else:
            super().enter_passengers(num)
