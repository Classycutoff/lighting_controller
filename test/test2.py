import serial
from serial.tools.list_ports import comports


class DMXConnection:
    def __init__(self, dmx_size=24, port="COM3", baudrate=250000):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

        self.dmx_size = dmx_size
        self.channels = bytearray(self.dmx_size)
        self.signal_start = bytearray([0x00, 0x00])
        self.signal_end = bytearray([0xE7])

    def open(self):
        self.serial = serial.Serial(self.port, baudrate=self.baudrate)

    def close(self):
        if self.serial is not None:
            self.serial.close()
            self.serial = None

    def send_dmx_message(self, msg):
        if self.serial is None or not self.serial.is_open:
            print("DMX connection is not open.")
            return False

        # self.serial.write(msg)

        dmx_message = bytearray(msg, "utf-8")

        # # dmx_message = self.signal_start + bytearray([0xFF] * 30) + self.signal_end
        self.serial.write(dmx_message)
        print(dmx_message)

        response = self.serial.read(self.serial.in_waiting).decode()
        print(response)
        return response


ports = comports()
port = ports[0].device
conn = DMXConnection()
conn.open()

# test_array = bytearray(
#     [
#         0x41,
#         0x72,
#         0x74,
#         0x2D,
#         0x4E,
#         0x65,
#         0x74,
#         0x00,
#         0x00,
#         0x50,
#         0x00,
#         0x0E,
#         0x00,
#         0x01,
#         0x00,
#         0x00,
#         0x02,
#         0x00,
#         0x8,
#     ]
# )
dmx_message = "".join(
    [
        "Art-Net\x00",
        "\x00",
        "\x00",
        "\x0e",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x02",
        "\x00",
        "\x08",
        "\xff",
        "\xff",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x09",
        "\x00",
        "\x00",
        "\x09",
        "\xc5",
        "\x00",
        "".join(["\x09"] * 495),
    ]
)


conn.send_dmx_message(dmx_message)
conn.close()

"""
dmx_message = array_to_send = "".join(
    [
        "Art-Net\x00",
        "\x00P",
        "\x00",
        "\x0e",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x02",
        "\x00",
        "\x08",
        "\xff",
        "\xff",  # channel 1,2,3
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",
        "\x00",  # channels 4-11
        "\x09",
        "\x00",
        "\x00",  # channel 12,13,14
        "\x09",
        "\xc5",
        "\x00",  # channle 15,16,17
        "".join(["\x09"] * 495),  # writes to remaining channels, 512 total
    ]
)
"""
