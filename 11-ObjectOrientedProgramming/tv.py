# The class should contain one boolean attribute called is_on that specifies whether the TV set is turned on. 
# Initially, the TV is turned off. 
# Add turn_on() and turn_off() methods in the class to turn the TV on and off, respectively. 
# Also, add a show_status() method to print whether the TV is on or off. 

# tv.py file
# class definition

class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def set_channel(self, new_channel_no):
        new_channel = new_channel_no
        self.channel_no = new_channel
    def set_channels(self, channels_list):
        self.channels = channels_list
    def show_channels(self):
        print("Channel list: ")
        print(*self.channels, sep="\n")
    def volume_increase(self):
        if self.volume >=0 and self.volume < 10:
            self.volume += 1
    def volume_decrease(self):
        if self.volume >=0 and self.volume < 10:
            self.volume -= 1

    def show_status(self):
        if self.is_on == True:
            if self.channel_no <= len(self.channels):
                print(f"The TV is on, channel {self.channel_no}, {self.channels[self.channel_no - 1]}, volume: {self.volume}")
            else:
                print(f"The TV is on, channel {self.channel_no}, volume: {self.volume}")
        else:
            print(f"The TV is off")


