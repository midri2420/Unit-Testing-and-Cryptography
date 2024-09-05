# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_word = ""
    for letter in text:
        letter_index = alpha.index(letter)
        new_word += codebet[letter_index]
    return new_word


def sub_decode(text, codebet):
    new_word = ""
    for letter in text:
        letter_index = codebet.index(letter)
        new_word += alpha[letter_index]
    return new_word


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
