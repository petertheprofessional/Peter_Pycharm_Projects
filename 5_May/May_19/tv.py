class tv:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True
        return "The TV is on"


    def turn_off(self):
        self.turned_on = False
        return "The TV is off"

    def channel_up(self):
        if self.channel <= 100 and self.channel >= 1:
            self.channel = self.channel + 1
            # return self.channel
            print(f"The channel is {self.channel}")

    def channel_down(self):
        if self.channel <= 100 and self.channel >= 1:
            self.channel = self.channel - 1
            # return self.channel
            print(f"The channel is {self.channel}")

    def set_channel(self, number):
        if number <= 100 and number >= 1:
            self.channel = number
            #return self.channel
            print(f"You selected channel {self.channel}")

    def volume_up(self):
        if self.volume_level <= 100 and self.volume_level >= 1:
            self.volume_level = self.volume_level + 1
            # return self.volume_level
            print(f"The volume is {self.volume_level}")

    def volume_down(self):
        if self.volume_level <= 100 and self.volume_level >= 1:
            self.volume_level = self.volume_level - 1
            # return self.volume_level
            print(f"The volume is {self.volume_level}")
