from DMXClient import DMXClient
import time


dmxClient = DMXClient("DMX_Pipe")

dmxClient.connect(True)
dmx_channel = 0

counter = 0

while True:
    try:
        dmxClient.write(
            {dmx_channel + 1: 255, dmx_channel + 1: 255}
        )  # DMX is counted from 1 upwards, and that's why it is + 1.
        counter += 1
        if counter % 5:
            dmx_channel += 1
            dmx_channel = dmx_channel % 12
    except KeyboardInterrupt as k:
        print(k)
        dmxClient.close()
        break


dmxClient.close()
