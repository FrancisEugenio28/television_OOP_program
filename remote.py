from Television import *

tv1 = television('ON', 1, 1)
# print all the instances from the character
print(tv1.TV_status(), tv1.get_channel(), tv1.get_volume())

# modify instance variables
tv1.status = 'OFF'
tv1.channel = 69
tv1.volume = 50
print("your TV is currently", tv1.status,". Also it's on channel", tv1.channel,"with a volume level of", tv1.volume)

# Add the channel 
tv1.channel_up()

# Minus the channel
tv1.channel_down()

# Add the volume
tv1.volume_up()

# Minus the volume
tv1.volume_down()