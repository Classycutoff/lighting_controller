import time
import utils._global as _global
from utils.audio_tools import get_audio_stream
from effects.DMX_Effects import *


def turn_on_all():
    if _global.is_on:
        _global.result_dmx_dict = {i: 0 for i in range(1, 25)}
    else:
        _global.result_dmx_dict = {i: 255 for i in range(1, 25)}
    _global.is_on = not _global.is_on
    _put_dmx_data()


def audio_to_dmx():
    try:
        audio_stream_var, dmx_values = get_audio_stream(
            _global.stream, _global.divided_freq_chunks
        )
        _global.result_dmx_dict = dmx_values
        _global.dmxClient.write_DMX(_global.result_dmx_dict)

        _global.stream, _global.divided_freq_chunks = audio_stream_var
        # Loop and delay to not overwhelm the other side of the dmxserver
        _global.root.after(20, func=lambda: audio_to_dmx())
    except KeyboardInterrupt as k:
        print(k)
        _global.dmxClient.close()
    except Exception as e:
        print(repr(e))
        _global.dmxClient.close()
        raise e


def wave_effect():
    # counter, beginning_dict, end_dict = ef_rgb_slow_forward_backward(
    #     beginning_dict, end_dict, counter, 24
    # )
    return True


def _put_dmx_data():
    try:
        _global.dmxClient.write_DMX(_global.result_dmx_dict)
        _global.root.after(40, func=lambda: _put_dmx_data())
    except KeyboardInterrupt as k:
        print(k)
        _global.dmxClient.close()
    except Exception as e:
        print(e)
        _global.dmxClient.close()
        raise e
