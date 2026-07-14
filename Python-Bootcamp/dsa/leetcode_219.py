from collections import defaultdict
nums = [1,0,1,1]
k = 1

groups = defaultdict(list)

for i, item in enumerate(nums):
    groups[item].append(i)

for item in groups:
    print(groups[item])