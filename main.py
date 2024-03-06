import time

from utils.DMXClient import DMXClient
from utils.audio_tools import get_audio_stream
from effects.DMX_Effects import ef_all_on, ef_rotate, ef_forward_backward
from effects.DMX_Effects import *


dmx_channel = 0
counter = 0
dmx_dict = {0: 255, 1: 255, 2: 255}
test = {}


def main():
    stream, divided_freq_chunks = (False, False)
    dmxClient = DMXClient("DMX_Pipe")
    KEEP_CONNECTION_UP = True
    try:
        while True:
            beginning_dict = dmx_dict
            end_dict = dmx_dict
            try:
                dmxClient.connect()
                while True:
                    # dmxClient.write_DMX(
                    #     {dmx_channel + 1: 255, dmx_channel + 1: 255}
                    # )  # DMX is counted from 1 upwards, and that's why it is + 1.

                    # dmx_dict = ef_all_on()

                    audio_stream_var, dmx_values = get_audio_stream(
                        stream, divided_freq_chunks
                    )
                    # counter, beginning_dict, end_dict = ef_rgb_slow_forward_backward(
                    #     beginning_dict, end_dict, counter, 24
                    # )
                    # dmx_dict = ef_forward_backward(dmx_dict, 24)
                    # test = ef_rgb_forward_backward(test, 24, 3)
                    # print("test", test)
                    # print(dmx_dict)
                    # result = beginning_dict | end_dict
                    # print(result)

                    # dmxClient.write_DMX(result)
                    dmxClient.write_DMX(dmx_values)

                    time.sleep(
                        0.04
                    )  # Added so that KeyBoardInterrupt has time to work.
                    stream, divided_freq_chunks = audio_stream_var
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


if __name__ == "__main__":
    main()
