#!/usr/bin/python
import sys

path = str(sys.argv[1])
outfile = open("utf8encoder_out.txt" , "wb")
infile = open(path , "rb")

# for i in range(0,6):
#     twobytes = infile.read(2)
#     print bin(ord(twobytes[0])),"|",bin(ord(twobytes[1])),"|"
#     byte0 = ord(twobytes[0])
#     byte1 = ord(twobytes[1])
#     byte2 = byte0*256 + byte1
#     print "byte0: ",byte0," | byte1: ",byte1," | byte2: ",byte2

#     if byte2 >= 0x0000 and byte2 <= 0x007F:
#         print "got here too!"
#         output = bytearray([0])
#         output[0] = byte1 & ~(1 << 7)
#         outfile.write(output)

#     else:
#         print "got here!"
#         output = bytearray([0xC0, 0x80])
#         temp = 63 & ord(twobytes[1])
#         output[1] = output[1] | temp
#         temp = 0xC0 & ord(twobytes[1])
#         temp = temp >> 6
#         byte1 = ord(twobytes[0]) << 2
#         temp1 = temp | byte1
#         output[0] = output[0] | (temp1 & 31)
#         outfile.write(output)

# infile.close()
# outfile.close()
# ------------------------------------

with open(path, "rb") as fo:
    bytedata1 = fo.read(2)
    # print "bytedata1[:2]: " + bytedata1
    while bytedata1 != b"":
        byte1 = ord(str(bytedata1[0]))
        byte2 = ord(str(bytedata1[1]))
        byte3 = ( byte1 * 256 ) + byte2
        if byte3 >= 0x0000 and byte3 <= 0x007F:
            output = bytearray([0])
            output[0] = byte2 & ~(1 << 7)
            outfile.write(output)

        elif byte3 >= 0x0080 and byte3 <= 0x07FF:
            output = bytearray([0xC0, 0x80])
            temp = 63 & byte2
            output[1] = output[1] | temp
            temp = 0xC0 & byte2
            temp = temp >> 6
            byte1 = byte1 << 2
            temp1 = temp | byte1
            output[0] = output[0] | (temp1 & 31)
            outfile.write(output)

        elif byte3 >= 0x0800 and byte3 <= 0xFFFF:
            output = bytearray([0xE0, 0x80, 0x80])
            temp = 63 & byte2
            output[2] = output[2] | temp
            temp1 = (byte2 & 0xC0) >> 6
            temp2 = byte1 & 0x0F
            temp3 = temp2 << 2
            temp3 = temp3 | temp1
            output[1] = output[1] | temp3
            temp4 = byte1 >> 4
            output[0] = output[0] |temp4
            outfile.write(output)

        bytedata1 = fo.read(2)

# fo.close()
outfile.close()

