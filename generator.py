import random
import string


def string_generator(length):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(length))


def email_generator():
    return string_generator(5)+'@gmail.com'