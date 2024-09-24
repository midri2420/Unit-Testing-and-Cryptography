import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    new_word = ""
    if len(text) == 0:
        return new_word
    elif a == 0:
        return new_word
    elif b == 0:
        return new_word
    text = text.upper()
    for i in range(len(text)):
        new_word += alpha[((((alpha.index(text[i])) * a) % 26) + b) % 26]
    return new_word

def affine_decode(text, a, b):
    new_word = ""
    if len(text) == 0:
        return new_word
    text = text.upper()
    for i in range(len(text)):
        new_word += alpha[((alpha.index(text[i]) - b) * mod_inverse(a, 26)) % 26]
    return new_word

# test = "HELLOWORLD"
# a = 5
# b = 9
# enc = affine_encode(test, a, b)
# dec = affine_decode(enc, a, b)
# print(enc)
# print(dec)
# # If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    ngram is text
    converts a piece of text into a number by multiplying it by
    26 ^ (index of letter), then sums it all.
    """
    num = 0
    if len(ngram) == 0:
        return num
    ngram = ngram.upper()
    for i in range(len(ngram)):
        num += alpha.index(ngram[i]) * (26 ** i)
    return num

def convert_to_text(num):
    """
    num is an ngram in numerical form
    converts a number back to a piece of text by floor dividing it by 26
    and then modding by 26 to find the remainder and using that as the new index,
    it goes until the floor division is == 0 meaning there is no remainder
    """
    new_word = ""
    if num == 0:
        return new_word
    new_word += alpha[(num % 26)]
    while num // 26 != 0:
        num = num // 26
        new_word += alpha[(num % 26)]
    return new_word

# test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
# l = len(test)
# num = convert_to_num(test)
# answer = convert_to_text(num)
# print(num)
# print(answer)
# # If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    """
    encodes a piece of text by slicing the tet into segments the length of n, and
    adding X's if not evenly divisible, then multiplies each n-gram in numerical
    representation by calling convert_to_num() by a, and adding b to it. then mods
    by 26 ^ n and converts back from a number to text using convert_to_text()
    """
    new_word = ""
    if len(text) // n != 0:
        text += "X" * (n - (len(text) % n))
    num_ngram = len(text) // n
    for i in range(num_ngram):
        first_index = i * n
        slicedngram = text[first_index: first_index + n]
        x = convert_to_num(slicedngram)
        new_word += convert_to_text((((a * x) + b) % (26 ** n)))
    return new_word


def affine_n_decode(text, n, a, b):
    """
    does a decode based on the above algorithm but in reverse, n, a, b are
    still the same
    """
    new_word = ""
    num_ngram = int((len(text) / n))
    for i in range(num_ngram):
        first_index = i * n
        slicedngram = text[first_index: first_index + n]
        for j in range(len(slicedngram)):
            x = convert_to_num(slicedngram)
            newindex = ((x - b) * mod_inverse(a, 26 ** n)) % (26 ** n)
        new_word += convert_to_text(newindex)
    return new_word


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 3#347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
print(affine_n_encode("HELLO", 3, 3, 121))
# If this worked, dec should be the same as test!

