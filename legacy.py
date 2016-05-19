#!/usr/bin/python
import sys
fo = open("out.txt", "wb")
with open(sys.argv[1], "rb") as f:
    byte2 = f.read(2)
    while byte2 != "":
        x = 256*ord(byte2[0]) + ord(byte2[1])
        if x >= 0x0000 and x <= 0x007F :
            rb1 = ord(byte2[1])
            b = bytearray([0])   # init
            b[0] = rb1 & ~(1<<7)
            fo.write(b)
        elif x >= 0x0080 and x <= 0x07FF :
            b = bytearray([0xC0 , 0x80])   # init
            rb2 = ord(byte2[1])
            rb2 = 63 & rb2
            b[1] = b[1] | rb2
            rb2 = ord(byte2[1])
            rb2 = 0xC0 & rb2
            rb2 = rb2 >> 6
        byte2 = f.read(2)