import random
import string


def generate_random_letter():
    return random.choice(string.ascii_lowercase)


def generate_three_letters() -> str:
    value = ""
    for _ in range(3):
        value += generate_random_letter()
    return value


print(generate_three_letters())
