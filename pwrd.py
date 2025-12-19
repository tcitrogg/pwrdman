import random
import string
import json
import os

SECRET_FILE = ".VAULT.pwrd"

class Pwrd:
    def __init__(self):
        # confirm if our dbfile exists
        if not os.path.exists(SECRET_FILE):
            json.dump({}, open(SECRET_FILE, "w"))

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
    
    def fetch_account(self, account_name):
        content = json.load(open(SECRET_FILE))
        if account_name in content:
            return content[account_name]
        else:
            return False

    def store(self, account_name, username, password):
        content = json.load(open(SECRET_FILE))
        content[account_name] = {"username":username, "password":password}
        json.dump(content, open(SECRET_FILE, "w"))