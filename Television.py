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
            print("The TV is", self.status)
# Determine the current channel
    def get_channel(self):
        print ("You're currently at the channel num.", self.channel)
        # Setting the channel to another channel
        retry = input("Do you wish to change a channel? Y/N: ").upper()
        if retry == 'Y':
            change_channel = input(int("What channel do you want?: "))
            return self.channel
        else:
            pass
# Determine the current volume of the TV
# Setting the volume to another VolumeLevel
# Channel UP
# Channel DOWN
# Volume UP
# Volume DOWN

TV1 = television('ON', 2, 5)
TV1.TV_status()
TV1.get_channel()

