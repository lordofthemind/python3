import string
import random

character = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def rndGenPwd():
    passLen = int(input("How long would you like your password to be: "))
    random.shuffle(character)

    password = []
    for x in range(passLen):
        password.append(random.choice(character))

    random.shuffle(password)
    password = "".join(password)

    print(password)

rndGenPwd()