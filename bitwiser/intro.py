

uni = [ord(character) for character in "abcdefg"]
print(uni)

bit_len = (42).bit_length()
print(bit_len)

len("€uro".encode("utf-8"))

for char in "€uro":
    print(char, len(char.encode("utf-8")))

