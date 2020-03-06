import random
import string


def generate_random_letter(): return random.choice(string.ascii_lowercase)


def generate_three_letters():
    value = ""
    for letter in range(3):
        value += generate_random_letter()
    return value


print(generate_three_letters())
