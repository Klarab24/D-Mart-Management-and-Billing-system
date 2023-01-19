#barcode scanner module
import serial as s
import time
import sys

class BarcodeScanner:
    def __init__(self):
        self.ser = s.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.ser.flush()

    def read(self):
        self.ser.flush()
        self.ser.write('r')
        time.sleep(0.5)
        return self.ser.readline()

    def close(self):
        self.ser.close()
    
    def __del__(self):
        self.close()

if __name__ == "__main__":
    scanner = BarcodeScanner()
    while True:
        try:
            barcode = scanner.read()
            print(barcode)
        except KeyboardInterrupt:
            scanner.close()
            sys.exit()