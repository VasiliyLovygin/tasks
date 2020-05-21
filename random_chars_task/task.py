import string
from itertools import product

chars = string.digits + string.ascii_letters


def word_generator(len_):
    for word_len in range(len_ + 1):
        for c in product(chars, repeat=word_len):
            yield "".join(c)


for word in word_generator(7):
    print(word)
