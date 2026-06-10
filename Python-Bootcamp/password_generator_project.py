import random
import string
import secrets


def generate_password(letters, symbols, digits):
    password = []
    for i in range(letters):
        password.append(secrets.choice(string.ascii_letters))
    for i in range(symbols):
        password.append(secrets.choice(string.punctuation))
    for i in range(digits):
          password.append(str(secrets.randbelow(10)))

    random.shuffle(password)
    print(''.join(password))

(generate_password(
        int(input("How many letters would you like?: ")),
        int(input("How many symbols would you like?: ")),
        int(input("How many digits would you like?: "))
))