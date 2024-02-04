from DMXClient import DMXClient
import time


dmxClient = DMXClient("DOPU")

dmxClient.connect(True)

while True:
    try:
        dmxClient.write({4: 255, 12: 255})
    except KeyboardInterrupt as k:
        print(k)
        break


dmxClient.close()
