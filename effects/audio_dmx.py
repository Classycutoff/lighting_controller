import numpy as np

import utils._global as _global


def normalize_to_dmx(x, newRange=(0, 1)) -> list[int]:
    xmin, xmax = np.min(x), np.max(x)  # get max and min from input array
    norm = (x - xmin) / (xmax - xmin)  # scale between zero and one

    if newRange == (0, 1):
        return norm  # wanted range is the same as norm
    else:
        return (
            norm * (newRange[1] - newRange[0]) + newRange[0]
        )  # scale to a different range.
    # add other conditions here. For example, an error message


def one_chan_to_three(dmx_values):
    result_values = {}
    for one_chan, value in dmx_values.items():
        if value <= 85:
            off_count = 0
        elif value <= 171:
            off_count = 1
        else:
            off_count = 2
        for i in range(one_chan * 3, one_chan * 3 + 4):
            if (i + off_count) % 3 == 0:
                result_values[i] = value
            else:
                result_values[i] = 0
    return result_values


def audio_to_dmx(audio_data):
    norm_to_dmx = normalize_to_dmx(audio_data, (0, 255))
    one_chan_dmx_values = {
        i + 1: round(audio_var) for i, audio_var in enumerate(norm_to_dmx)
    }
    dmx_values = one_chan_to_three(one_chan_dmx_values)
    return dmx_values
