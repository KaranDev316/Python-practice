import random
import string

number_of_letters = int(input("How many letters would you like?: "))
number_of_symbols =int(input("How many symbols would you like?: "))
number_of_digits = int(input("How many digits would you like?: "))

letters = ""
symbols = ""
digits =""

for i in range(number_of_letters):
    letters += random.choice(string.ascii_letters)
for i in range(number_of_symbols):
    symbols += random.choice(string.punctuation)
for i in range(number_of_digits):
      digits +=str(random.randint(0, 9))


password = list(letters + symbols + digits)
random.shuffle(password)
print("".join(password))