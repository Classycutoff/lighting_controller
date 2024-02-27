def ef_rotate(dmx_dictx, mod_num, skip_light):
    if skip_light < 0:
        result_dict = {}
        for dmx_chan, value in dmx_dictx.items():
            if (dmx_chan + skip_light) <= 0:
                result_dict[mod_num - (dmx_chan + skip_light) + 1] = value
            else:
                result_dict[dmx_chan + skip_light] = value
    else:
        result_dict = {
            ((key + skip_light) % mod_num + 1): value
            for key, value in dmx_dictx.items()
        }
    return result_dict


def ef_all_on(dmx=None, chan_range=255):
    dmx_dict = {i: 255 for i in range(1, chan_range + 1)}
    return dmx_dict


# dmx is the dict with channel and value, dmx_range is what values do you want
def ef_forward_backward(dmx, dmx_range, chan_val=255):
    if len(dmx) != 2:
        # Returns the starting values for this effect, which is the first and last channel.
        return {1: chan_val, dmx_range: chan_val}
    dmx_items = list(dmx.items())
    forward_chan, forward_val = dmx_items[0]
    backward_chan, backward_val = dmx_items[1]

    forward_chan = forward_chan % dmx_range + 1
    backward_chan -= 1
    if backward_chan <= 0:
        backward_chan = dmx_range

    result_dict = {forward_chan: forward_val, backward_chan: backward_val}

    return result_dict


def slow_wrapper(mod_num, count, func, dmx_dict, args):
    count = count % mod_num
    if count == 0:
        return count, func(dmx_dict, *args)

    count += 1
    return count, dmx_dict


def ef_rgb_slow_forward_backward(beginning_dict, end_dict, counter, mod_num):
    bcount, beginning_dict = slow_wrapper(
        5, counter, ef_rotate, beginning_dict, [mod_num, 3]
    )
    ecount, end_dict = slow_wrapper(10, counter, ef_rotate, end_dict, [mod_num, -3])

    if not beginning_dict and not end_dict:
        raise ValueError

    return bcount, beginning_dict, end_dict
