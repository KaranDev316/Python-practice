from collections import defaultdict

words = [
    "apple",
    "ant",
    "banana",
    "boat",
    "car"
]

groups = defaultdict(list)

for word in words:
    groups[word[0]].append(word)

print(groups)