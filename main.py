import usb.core
import usb.util
import usb
import sys
from pyftdi.ftdi import Ftdi
from pyftdi.usbtools import UsbTools as ut
import pyftdi.serialext

"""
Decimal VendorID=1027 & ProductID=24577
Hexadecimal VendorID=0x403 & ProductID=0x6001
"""


def main():
    ID_VENDOR = 0x403
    ID_PRODUCT = 0x6001
    SERIAL_NUMBER = "AQ01UBVG"
    CONNECTION_URL = f"ftdi://{ID_VENDOR}:{ID_PRODUCT}:{SERIAL_NUMBER}/1"
    device_descriptor = Ftdi.list_devices()[0][0]
    # Ftdi.add_custom_vendor(ID_VENDOR)
    # Ftdi.add_custom_product(ID_VENDOR, ID_PRODUCT)

    # Find your usb with the find_usb.py file
    # dev = usb.core.find(ID_VENDOR=ID_VENDOR, ID_PRODUCT=ID_PRODUCT)

    # print("dev:", dev)
    # if dev is None:
    #     raise ValueError("Device not found")

    device_descriptor = Ftdi.list_devices()[0][0]

    dev = ut.get_device(device_descriptor)
    if dev is None:
        raise ValueError("Device not found")

    print(dev)

    port = pyftdi.serialext.serial_for_url(CONNECTION_URL, baudrate=3000000)
    port.write(b"Hello World")

    data = port.read(1024)

    # endpoint = dev[0].interfaces()[0].endpoints()[0]
    # interface_number = dev[0].interfaces()[0].bInterfaceNumber

    # print(dev)
    # if dev.is_kernel_driver_active(interface_number):
    #     dev.detach_kernel_driver(interface_number)

    """endpoint = dev[0].interfaces()[0].endpoints()[0]
    interface_number = dev[0].interfaces()[0].bInterfaceNumber
    """

    """
    print(dev)
    if dev.is_kernel_driver_active(interface_number):
        dev.detach_kernel_driver(interface_number)

    # dev.set_configuration()
    print(type(endpoint))
    print(interface_number)

    dev.set_configuration()
    eaddr = endpoint.bEndpointAddress
    
    cfg = dev.get_active_configuration()
    print(cfg)
    intf = cfg[(0, 0)]

    ep = usb.util.find_descriptor(
        intf,
        custom_match=lambda e:
        usb.util.endpoint_direction(e.bEndpointAddress) ==
        usb.util.ENDPOINT_OUT
    )

    assert ep is not None

    ep.write(1, 255)
    """

    return None


if __name__ == "__main__":
    main()
