import numpy as np

import utils._global as _global


# Depracated
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


def normalize_decibels(data):
    min = _global.DB_MIN
    max = _global.DB_MAX
    data = np.clip(data, min, max)

    normalized = (
        (np.log10(data) - np.log10(min)) / (np.log10(max) - np.log10(min))
    ) * 255
    normalized = np.clip(np.round(normalized), 0, 255)
    return normalized


def var_to_rgb_channels(dmx_values):
    color_bins = _global.COLOR_BINS
    colors_to_bins = _global.COLORS_TO_BINS
    result_values = {}
    for one_chan, value in dmx_values.items():
        bin_index = np.digitize(value, color_bins) - 1
        brightness = (value - color_bins[bin_index]) / (
            color_bins[bin_index + 1] - color_bins[bin_index]
        )
        color = colors_to_bins.get(bin_index, {"R": 0, "G": 0, "B": 0})
        colors_list_order = list(color.keys())
        channel = one_chan * 3
        for i in range(channel, channel + 4):
            col_lst_index = i % 3
            result_values[i + 1] = min(
                int(color[colors_list_order[col_lst_index]] * brightness), 255
            )
    return result_values


# Depracated
def one_chan_to_three(dmx_values):
    result_values = {}
    for one_chan, value in dmx_values.items():
        if value <= 125:
            off_count = 0
            value = value // 2
        elif value <= 235:
            off_count = 1
        else:
            off_count = 2
        for i in range(one_chan * 3, one_chan * 3 + 4):
            if (i + off_count) % 3 == 0:
                result_values[i + 1] = value
            else:
                result_values[i + 1] = 0
    return result_values


def audio_to_dmx(audio_data):
    norm_to_dmx = normalize_decibels(audio_data)
    one_chan_dmx_values = {i: int(audio_var) for i, audio_var in enumerate(norm_to_dmx)}
    dmx_values = var_to_rgb_channels(one_chan_dmx_values)
    return dmx_values
