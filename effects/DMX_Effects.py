def ef_rotate(dmx, mod_num):
    result_dict = {(key % mod_num + 1): value for key, value in dmx.items()}
    return result_dict


def ef_all_on(dmx=None, chan_range=255):
    dmx_dict = {i: 255 for i in range(1, chan_range + 1)}
    return dmx_dict
