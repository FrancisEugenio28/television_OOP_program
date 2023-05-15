#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Assignment 6

# create class for television
class television:
    # constructor
    def __init__(self, status, channel, volume):
        self.status = status
        self.channel = channel
        self.volume = volume
        
# Television ON
    def status_ON(self):
        print("The TV is", self.status)
# Television OFF
    def status_OFF(self):
        print("The TV is", self.status)
# Determine the current channel
    def get_channel(self):
        print ("Your currently at the channel num.", self.channel)
# Setting the channel to another channel
# Determine the current volume of the TV
# Setting the volume to another VolumeLevel
# Channel UP
# Channel DOWN
# Volume UP
# Volume DOWN

TV = television('OFF', 2, 5)
TV.status_ON()
TV.get_channel()