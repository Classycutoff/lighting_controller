import usb.core
import usb.util
import usb
import sys


def main():
    # Find your usb with the find_usb.py file
    dev = usb.core.find(idVendor=0x403, idProduct=0x6001)

    if dev is None:
        raise ValueError("Device not found")

    # dev.set_configuration()

    cfg = dev.get_active_configuration()
    intf = cfg[(0, 0)]

    ep = usb.util.find_descriptor(
        intf,
        custom_match=lambda e:
        usb.util.endpoint_direction(e.bEndpointAddress) ==
        usb.util.ENDPOINT_OUT
    )

    assert ep is not None

    ep.write(1, 255)


if __name__ == "__main__":
    main()
