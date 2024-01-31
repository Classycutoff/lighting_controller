from DMXClient import DMXClient
import time


dmxClient = DMXClient("DOPU")

dmxClient.connect(True)

while True:
    try:
        dmxClient.write({1: 255, 2: 255})
        time.sleep(1)
    except KeyboardInterrupt as k:
        print(k)
        break


dmxClient.close()
