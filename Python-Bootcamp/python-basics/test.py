from collections import Counter
strings = ["cat", "dog", "cat", "bird", "dog", "fish"]



freq = Counter(strings)

print(freq)
print(freq["dog"])
print(freq["bird"])