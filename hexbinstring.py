#https://stackoverflow.com/questions/1425493/convert-hex-to-binary

integer = int('ABC123EFFF', 16)
print(integer)

integer = 0xABC123EFFF
print(integer)

#doesn't work
# hex_string = '0x1A23'
# integer = hex(hex_string)
# print(integer)

hex_string = '0x1A23'
print(hex_string)

t = int(hex_string, 16)
print(t)


