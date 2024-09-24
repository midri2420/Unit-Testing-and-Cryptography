import math

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def mod_inverse_helper(a, b):
  q, r = a // b, a % b
  if r == 1:
    return (1, -1 * q)
  u, v = mod_inverse_helper(b, r)
  return (v, -1 * q * v + u)

def mod_inverse(a, m):
  assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
  return mod_inverse_helper(m, a)[1] % m

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

# Also write these:
def rsa_encode(text, m, e):
  x = convert_to_num(text)
  assert x < m, "text is too long"
  return pow(x, e, m)

def rsa_decode(num, m, d, l):
  decode = pow(num, d, m)
  return convert_to_text(decode)

def get_d(p, q, e):
  t = (p - 1) * (q - 1)
  return mod_inverse(e, t)

text = "THEFIVEBOXINGWIZARDSJUMPQUICKLY"
l = len(text)
p = 292361466231755597564095925310764764819
q = 307125506157764866722739041634199200019
e = 65537
m = p * q
d = get_d(p, q, e)
print(d)
enc = rsa_encode(text, m, e)
dec = rsa_decode(enc, m, d, l)
print(enc)
print(dec)
# If this works, dec should be the same as text!


# Part 2: Generate your own key!

# from sympy import nextprime
# from random import randint
#
# def make_prime(n):
#   lower = 2 ** (n - 1) + 1
#   upper = 2 ** n - 1
#   temp = randint(lower, upper)
#   return nextprime(temp)
#
# make_prime(512)
