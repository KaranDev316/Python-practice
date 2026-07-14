from collections import Counter
arr = [2,2,1,1,3]
result  = set()
counts = Counter(arr)

for key, item in counts.items():
    result.add(item)

print(result)