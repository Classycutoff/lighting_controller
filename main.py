import time

from tools.DMXClient import DMXClient
from effects.DMX_Effects import ef_all_on, ef_rotate, ef_forward_backward
from effects.DMX_Effects import *

dmxClient = DMXClient("DMX_Pipe")
KEEP_CONNECTION_UP = True

dmx_channel = 0
counter = 0
dmx_dict = {0: 255}
test = {}

try:
    while True:
        try:
            dmxClient.connect()
            while True:
                # dmxClient.write_DMX(
                #     {dmx_channel + 1: 255, dmx_channel + 1: 255}
                # )  # DMX is counted from 1 upwards, and that's why it is + 1.

                # dmx_dict = ef_all_on()
                # dmx_dict = ef_rotate(dmx_dict, 24)
                dmx_dict = ef_forward_backward(dmx_dict, 24)
                test = ef_rgb_forward_backward(test, 24, 3)
                print(test)
                # print(dmx_dict)

                dmxClient.write_DMX(dmx_dict)

                time.sleep(0.04)  # Added so that KeyBoardInterrupt has time to work.
        except Exception as e:
            print(e)
            dmxClient.close()
            if not KEEP_CONNECTION_UP:
                break

            dmxClient = DMXClient("DMX_Pipe")


except KeyboardInterrupt as k:
    print(k)
    dmxClient.close()
except Exception as e:
    print(e)
    dmxClient.close()
    raise e


dmxClient.close()
