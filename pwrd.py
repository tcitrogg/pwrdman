import random
import string
import json

class Pwrd:
    def __init__(self):
        pass

    def gen_passwrd(self, l_len=6, n_len=1, s_len=1):
        """
            default:
            - 6 letters
            - 1 number
            - 1 symbol
        """
        letters = random.choices(string.ascii_letters, k=l_len)
        numbers = random.choices(string.digits, k=n_len)
        symbols = random.choices(string.punctuation, k=s_len)

        random_chars = letters + symbols + numbers
        random.shuffle(random_chars)

        passwrd = "".join(random_chars)

        return passwrd