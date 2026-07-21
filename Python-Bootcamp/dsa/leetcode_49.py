from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

group = defaultdict(list)
result = []
sorted_strs = set()
for str1 in strs:
    sorted_strs.add("".join(sorted(str1)))

for str2 in strs:
    if "".join(sorted(str2)) in sorted_strs:
        group["".join(sorted(str2))].append(str2)

for value in group.values():
    result.append(value)
print(result)