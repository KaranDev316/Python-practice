from collections import Counter
arr = [2,2,1,1,3]
result  = set()
counts = Counter(arr)
items = []

for _, item in counts.items():
    result.add(item)
    items.append(item)
    print(item)

if len(result) == len(items):
    print("Unique items in list")
else:
    print("Not Unique items in list")