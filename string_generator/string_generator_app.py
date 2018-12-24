import random
import string


def generate_random_letter(): return random.choice(string.ascii_lowercase)


def generate_three_letters():
    return generate_random_letter() + generate_random_letter() + generate_random_letter()


print(generate_three_letters())
