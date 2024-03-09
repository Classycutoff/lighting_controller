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
# dmx_message = "".join(
#     [
#         "Art-Net\x00",
#         "\x00",
#         "\x00",
#         "\x0e",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x02",
#         "\x00",
#         "\x08",
#         "\xff",
#         "\xff",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x00",
#         "\x09",
#         "\x00",
#         "\x00",
#         "\x09",
#         "\xc5",
#         "\x00",
#         "".join(["\x09"] * 495),
#     ]
# )


dmx_message_temp = """44fefc3cfc3cc738ff4042623f2121ff4422233d31114402231d8884c446623e11844446223f21114446423e2111c446423e2121ff4446423e2101c4466222f18844422221f18044422211fc8444426220f18c44464222e18c44464262a28444464223e18cc4464222e18044464222a18840222321f184448c844442e2c488848404c2c48c84c444c2448c848444c24488c44442e0448c84c444c24484444262e2c48c844442c244467a232121ff44223f21318c44427e232121ff44467a232121ff44467a622221ff44427e22311144427e223111c44642c28c84c44662a28cc4444622a38c84444622e38c84444222e184c4440223c18c84404262a38c84c44642c28cc4444262e38cc4444262e08cc4c4022321311fc4464222213dffc4422221211f4022232111f8444622018cf84446223d21ffc44642423e21ff402223213f11444262233d21ff444642623e21ff444642423e23ff444262233d21ff444642623e31ffc44642423e21ff444222213f11444642223d21ff4422233184fc444262233d21ff404262233d21ff444642623e21ff4042622331f44446626322e1c446420221e14446422221d14446426222e1ccfafafa4cfefefa4cfa7efa4cfafafa4cfefafacc7efafa4cfafafa4cfa7efaccfafafaccfafafa4cfafafec8fafafaccfefafac8fabefa4c7efafa4cfafafe4cfa7efa4cfafefa4c7efafac8fefefaccfefefe4cfa7afa4c7e7ebe4c7e7efaccfa7efe4cfafefe4cfafafaccfafebeccfefafaccfafafaccfefa7eccfafafa4cfa7efa4cfefefaccfafefaccfefafe4cfafefa4cfe7efac8fefa7e4cfabafe4cfafafaccfafefa4cfa7efe4c7efafa4cfaf6faccfefafaccfefafa4cfafa7eccfafa7e4cfa7efa4cfafa7e4cfafafe4cfafefac8fafafa4cfa7efa4c7efafe4cfafefeccfafafa4cfafefa4cfe7efaccfafefaccfafabecc7efafec44642222121ff40c262236121ff4cc262233111444662272121ff4882230184c44c4642276121ff44426222311144464220118c4cc66223e121ff44466227211144422225718c4c464226a31154462231b111d4422221a1115cc22233318c54422225518854462231118c5c462223518c54422235a11154422225118cdc462221018c54462225518c54462225a11148c22225e131c4422121918c444231118c8450c22123918c584231138c8ccc4662266121ffcc464246a21144462135508844422111b4c44cc22137918044462125d18c4446218dd4c44c4621139c8454462115a8845446212191845c462133718854422101b88454463117bc845c462133f11154462135518c54462115b4c45c462117a88454462135a111d4822117b0c2dcc62137d184644642722031ff6442622221314022114446e264466227711064422229918c6cc26221711164464222a33164464232a3116cc26223318c64464232a331ffec46023f518c6ca231139c8474463115ac847c463115ac847c46314446e0f446118ae4c47c46313117fc7c46113117f87446311594c4fc46111131ff7cc2313115fc74463117bc847c463117bc84fc463117b884e44642222331ff6cc2314556c26c4642766031644642722231ff447ec28c84447ae28c88447ae28c884c7e4244444c3aa3c444c476c28c8c4476c28c84cc764242424c76424242447ec28d8d443223058d4c7ec2c2c2403a2322c2c476428d47f64472228947f6cc764242424c76424242546ea28888547e628c8c5cfea2444444722144445466a28c8cd466a28c8c5c7622a2a25c66a2a220547262894bf65432238d43f2dc6e2222a2dc6e222222d466608dd7e65466228dd7e65cf6222222dc66222222447ef18888446ee2848850eaa14545503aa145454476c2888844bee18c804cf6a14242cc76424646447ee18d8d4462f18d85cc7ea1a1a14c6e61a1a144a2e18d46f64466e18d46e6cc76a121a14ce6a1a131547a618843f6546e618c43f6dcee61c557ea5ceea14547f2d466218c43f65c6a618c43f6dc6621a3a15c66213121546e618d4bf65072618d4bf65c322121215c32217121d466618dd6e65466618dd6e65ce6212121dc66212121647ec28a8a647ec28e8eecfee244406c7e42c44448aeb18e8e646ae28e8e48aa514343ec76424343e47e028f8f647ec2078f40fcf1c2226c7ec2c2c26476228fe7f6e476028b67f66c764242426c76424242747af18e8e742671068e402ad144447cfef184447476518e8e746a318e8a7c66b1b1b1fc66b1b1b1746ef18f42f2f46ef18f42e67c6ef171317c3211f1717476b18b77f2f4b2b18f4be67cf2b111b17c76b1b131646a510623ff647ec22335716c6e42299fd4ec7e42277571e47642273151e476c2233131587a314327f56ce6314327f1647e718723f5647e118f23f56c7e1111716c6e7111716476318f66e65862310be6e26ce23131316c663131b1742a518e53e6746e718e53f47c6e714557f250ea514557f27466318e53f67466318e13f77c665131317c66313131746e718b56e2746e718f52f6"""

base16INT = int(dmx_message_temp, 16)


dmx_message = hex(base16INT)

conn.send_dmx_message(dmx_message)
conn.close()
