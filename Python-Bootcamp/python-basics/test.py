from collections import defaultdict

d = defaultdict(list)

for ch in "banana":
    d[ch].append(ch.upper())
print(d["b"])