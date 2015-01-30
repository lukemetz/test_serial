import serial

class Serial(serial.Serial):
    def write(self, *kwargs):
        print kwargs
        print "wrote to serial"
        super(Serial, self).write(*kwargs)

import xbee
import sys

if __name__ == "__main__":
    ser = Serial(sys.argv[1], timeout=0, baudrate=230400)
    xb = xbee.XBee(ser)
    xb.tx(dest_addr = '\x00\x15', data="HELLO")

