from DMXClient import DMXClient
import time


dmxClient = DMXClient("DMX_Pipe")

dmxClient.connect()
dmx_channel = 0

counter = 0

while True:
    try:
        # dmxClient.write_DMX(
        #     {dmx_channel + 1: 255, dmx_channel + 1: 255}
        # )  # DMX is counted from 1 upwards, and that's why it is + 1.
        dmxClient.write_DMX({4: 255, 5: 255})
        counter += 1
        if counter % 5:
            dmx_channel += 1
            dmx_channel = dmx_channel % 12
    except KeyboardInterrupt as k:
        print(k)
        dmxClient.close()
        break
    except Exception as e:
        print(e)
        dmxClient.close()
        dmxClient = DMXClient("DMX_Pipe")
        dmxClient.connect()


dmxClient.close()
