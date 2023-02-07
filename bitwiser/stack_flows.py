value1 = 0x01
value2 = 0x02
value3 = 0x03
value4 = 0x04
value5 = 0x05
value6 = 0x06
value7 = 0x40
value8 = 0x80

def parse_byte(byte):
    return byte & value7, byte & 0x80, byte & 7

# Example 1
byte = value3 | value7
value7_set,value8_set,base_value = parse_byte(byte)
print("base_value = "+str(base_value))
if value7_set: print("value7_set")
if value8_set: print("value8_set")
print()

# Example 2
byte = value5
value7_set,value8_set,base_value = parse_byte(byte)
print("base_value = "+str(base_value))
if value7_set: print("value7_set")
if value8_set: print("value8_set")
print()

# Example 3
byte = value1 | value7 | value8
value7_set,value8_set,base_value = parse_byte(byte)
print("base_value = "+str(base_value))
if value7_set: print("value7_set")
if value8_set: print("value8_set")
print()