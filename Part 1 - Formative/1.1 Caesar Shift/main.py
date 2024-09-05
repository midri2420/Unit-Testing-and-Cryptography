# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_word = ""
    for letter in text:
        index = alpha.index(letter)
        new_word += alpha[(index + n) % 26]
    return new_word

# new_word += (alpha[((alpha.index(letter)) + n) % 26])

def caesar_decode(text, n):
    new_word = ""
    for letter in text:
        index = alpha.index(letter)
        new_word += alpha[(index - n) % 26]
    return new_word


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!

