from collections import Counter
s = "leetcode"
s2 = Counter(s)


seen = set()
duplicate = set()
result = 0

for item in s:
    if item in seen:
        duplicate.add(item)
    seen.add(item)
unique_items = seen - duplicate
print(unique_items)
for i, item in enumerate(s):
    if item in unique_items:
        result = i
        break

print(result)