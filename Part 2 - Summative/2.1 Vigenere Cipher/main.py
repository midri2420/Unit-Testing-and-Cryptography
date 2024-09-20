# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  new_word = ""
  text = text.upper()
  keyword = keyword.upper()
  if len(keyword) ==  0:
    return new_word
  for i in range(len(text)):
    new_word += alpha[(alpha.index(text[i]) + alpha.index(keyword[i % len(keyword)])) % 26]
  return new_word


def vig_decode(text, keyword):
  new_word = ''
  text = text.upper()
  keyword = keyword.upper()
  if len(keyword) ==  0:
    return new_word
  if len(keyword) == 0:
    return new_word
  for i in range(len(text)):
    new_word += alpha[(alpha.index(text[i]) - alpha.index(keyword[i % len(keyword)])) % 26]
  return new_word

test = ""
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!