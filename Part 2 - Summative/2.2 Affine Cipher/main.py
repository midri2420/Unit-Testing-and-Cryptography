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
    num = 0
    if len(ngram) == 0:
        return num
    ngram = ngram.upper()
    for i in range(len(ngram)):
        num += alpha.index(ngram[i]) * (26 ** i)
    return num

def convert_to_text(num):
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
    new_word = ""
    if len(text) // n != 0:
        text += "X" * (n - (len(text) % n))

    print(len(text))
    num_ngram = len(text) // n
    for i in range(num_ngram):
        first_index = i * n
        slicedngram = text[first_index: first_index + n]
        x = convert_to_num(slicedngram)
        print(convert_to_text((((a * x) + b) % (26 ** n))))
        new_word += convert_to_text((((a * x) + b) % (26 ** n)))
    print(len(new_word))
    return new_word


def affine_n_decode(text, n, a, b):
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
print(affine_n_encode("COOL", 3, 3, 121))
# If this worked, dec should be the same as test!


print(convert_to_num("RTHEL"))
# RTHEL IN NUMBER FORM IS 5102283
print(convert_to_text((((347 * 5102283) + 1721) % (26 ** 5))))
