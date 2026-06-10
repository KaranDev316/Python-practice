import random
import string
import secrets

number_of_letters = int(input("How many letters would you like?: "))
number_of_symbols =int(input("How many symbols would you like?: "))
number_of_digits = int(input("How many digits would you like?: "))

password = []
for i in range(number_of_letters):
    password.append(secrets.choice(string.ascii_letters))
for i in range(number_of_symbols):
    password.append(secrets.choice(string.punctuation))
for i in range(number_of_digits):
      password.append(str(secrets.randbelow(10)))

random.shuffle(password)
print(''.join(password))