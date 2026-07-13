from collections import defaultdict
target = 6
output = []
nums = [3,2,4]
seen = {}

for i, item in enumerate(nums):
    competence = target - item
    if competence in seen:
        output.append(seen[competence],i)
    seen[item] = i
print(output)