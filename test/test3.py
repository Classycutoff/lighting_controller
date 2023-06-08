import serial
import time

port = "COM3"
baud_rate = 96000


ser = serial.Serial(port=port, baudrate=baud_rate, timeout=1)

try:
    while True:
        data = ser.readline().hex()

        if data:
            print("Received data from serial port: ", data)
            time.sleep(0.5)

except KeyboardInterrupt:
    print("Closing the serial port.")
    ser.close()
