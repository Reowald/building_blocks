
import struct
import binascii
#
# d = '0xCDCC4842'
# b = struct.unpack('f', binascii.unhexlify('CD43'))

# a = bytearray.fromhex(d)

# b = struct.unpack('!f', bytes.fromhex('CDCC4842'))


# print(a)
# print(b)

# dd = '0x425c0000'
#
# q = int(d, 16)
# b8 = struct.pack('i', q)
# dec, = struct.unpack('f', b8)
#
# print(dec)

#
# Convert IEEE 754 64-bit Hex to Float
hexString = "0x43CD0000"
msg_dec = struct.unpack(">f", struct.pack("f",int(hexString, 16)))[0]

print(msg_dec)

# Convert IEEE 754 64-bit Float to Hex
decVal = 410.00
msg_hex = hex(struct.unpack(">f", struct.pack("f", decVal))[0])

print(msg_hex)

# def float_to_bin(num):
#     bits, = struct.unpack('!I', struct.pack('!f', num))
#     return "{:032b}".format(bits)
#
#
# num_bin = float_to_bin(410.00)
# num_hex = hex(int(num_bin))
#
# print(num_hex)
#
