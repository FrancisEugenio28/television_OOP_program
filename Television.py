#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Assignment 6

# create class for television
class television(self, status, channel, volume):
    # constructor
    def __init__(self):
        self.status = status
        self.channel = channel
        self.volume = volume
        
# Television ON
    def status_ON(self):
        print("The TV is ", self.status)
# Television OFF
# Determine the current channel
# Setting the channel to another channel
# Determine the current volume of the TV
# Setting the volume to another VolumeLevel
# Channel UP
# Channel DOWN
# Volume UP
# Volume DOWN

TV = television('television', 'ON')
TV.status_ON()