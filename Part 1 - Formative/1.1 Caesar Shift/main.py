# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_word = ""
    for letter in text:
        index = alpha.index(letter.upper())
        new_word += (alpha[(index + n) % 26]).upper()
    return new_word


def caesar_decode(text, n):
    new_word = ""
    for letter in text:
        index = alpha.index(letter.upper())
        new_word += (alpha[(index - n) % 26]).upper()
    return new_word


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!