from collections import defaultdict
nums = [1,0,1,1]
k = 1
seen = defaultdict(int)

for i, num in enumerate(nums):
    if num in seen:
        if abs(seen[num] -  i) <= k:
            print(True)
    seen[num] = i









