from collections import Counter
s = "aaaa"
p = "aa"


right = len(p)
sett = set()
for left in range(len(s)):

    if Counter(s[left:right]) == Counter(p):
        sett.add(left)
    right += 1

print(sett)

