# https://www.orangecoat.com/how-to/use-pyusb-to-find-vendor-and-product-ids-for-usb-devices

import usb.core
import usb.util
import usb
import sys

dev = usb.core.find(find_all=1)

i = 0
for cfg in dev:
    print(i)
    i += 1
    sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) +
                     ' & ProductID=' + str(cfg.idProduct) + '\n')
    sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) +
                     ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
