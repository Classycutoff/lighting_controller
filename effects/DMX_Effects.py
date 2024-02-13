def ef_rotate(dmx, mod_num):
    result_dict = {(key % mod_num + 1): value for key, value in dmx.items()}
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


# dmx is the dict with channel and value, dmx_range is what values do you want,
# dmx_range the range of channels starting from 1,
# chan_range is how many lights you want to put on at the same time.
# and chan_val is the value of the channel.
def ef_rgb_forward_backward(dmx, dmx_range, chan_range, chan_val=255):
    if len(dmx) != chan_range * 2:
        # Returns the starting values for this effect, which is the first and last channel.
        result_dict = {}
        for i in range(1, 1 + chan_range):
            result_dict[i] = chan_val
        for i in range(dmx_range, dmx_range - chan_range, -1):
            result_dict[i] = chan_val

        return result_dict

    result_dict = {}
    dmx_items = list(dmx.items())
    forward_lst = dmx_items[0:chan_range]
    for dmx_chan, dmx_val in forward_lst:
        result_dict[dmx_chan % dmx_range + 1] = dmx_val

    backward_lst = dmx_items[-1 * chan_range :]
    print(backward_lst)

    # forward_chan, forward_val = dmx_items[0]
    # backward_chan, backward_val = dmx_items[1]

    # forward_chan = forward_chan % dmx_range + 1
    # backward_chan -= 1
    # if backward_chan <= 0:
    #     backward_chan = dmx_range

    # result_dict = {forward_chan: forward_val, backward_chan: backward_val}

    return dmx
