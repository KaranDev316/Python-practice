# option + fn + F12 to open the terminal in mac
from random import seed

#Counting unique characters in a given string
s = 'abca'
seen_char = ''
count = 0
for char in s:
    if char not in seen_char:
        seen_char += char
        count += 1
print(count)


