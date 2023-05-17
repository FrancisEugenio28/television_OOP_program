#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Assignment 6

# create class for television
class television:
    # constructor
    def __init__(self, status, channel, volume,):
        self.status = status
        self.channel = channel
        self.volume = volume
        
# Television Status
    def TV_status(self):
        if self.status == 'ON':
            print("The TV is", self.status)
        else:
            print("The TV is OFF")
# Determine the current channel
    def get_channel(self):
        print ("You're currently at the channel num.", self.channel)
        # Setting the channel to another channel
        retry = input("Do you wish to change a channel? Y/N: ").upper()
        if retry == 'Y':
            self.channel = input(str("What channel do you want?: "))
            print ("You're currently at the channel num.", self.channel, "now")
            return self.channel
        else:
            pass
# Determine the current volume of the TV
    def get_volume(self):
        print ("You're current volume level is", self.volume)
        # Setting the volume to another VolumeLevel
        retry = input("Do you wish to change the volume? Y/N: ").upper()
        if retry == 'Y':
            self.volume = input(str("What volume level do you want?: "))
            print ("You're current volume level is", self.volume, "now")
            return self.volume
        else:
            pass
# Channel UP
    def channel_up(self):
        self.channel += 1 
        print("You're currently at the channel num.", self.channel, "now")
        return self.channel     
# Channel DOWN
    def channel_down(self):
        self.channel -= 1 
        print("You're currently at the channel num.", self.channel, "now")
        return self.channel     
# Volume UP
    def volume_up(self):
        self.volume += 1
        print ("You're current volume level is", self.volume, "now")
        return self.volume
# Volume DOWN
    def volume_up(self):
        self.volume -= 1
        print ("You're current volume level is", self.volume, "now")
        return self.volume



