class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.is_turned_on = False
    def turn_on(self):
        self.turned_on = True

    def turn_on(self):
        self.is_turned_on = False

    def switch_on_off(self):
        self.is_turned_on = not self.is_turned_on

    def channel_up(self):
        if self.is_turned_on:
            if self.channel + 1 < 100:
                self.set_channel(self.channel + 1)
                print(f"The channel is {self.channel}")

    def channel_down(self):
        if self.is_turned_on:
            if self.channel - 1 >= 0:
                self.set_channel(self.channel - 1)
                print(f"The channel is {self.channel}")

    def set_channel(self, channel_number):
        if self.is_turned_on:
            if channel_number > 0 and channel_number <= 100:
                self.channel = channel_number
                print(f"The channel is {self.channel}")

    def volume_up(self):
        if self.is_turned_on:
            if self.channel + 1 < 10:
                self.volume = self.volume +1
                print(f"The volume is {self.volume}")

    def volume_down(self):
        if self.is_turned_on:
            if self.channel - 1 > 0:
                self.volume -= 1
                print(f"The volume is {self.volume}")



