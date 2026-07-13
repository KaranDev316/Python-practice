from collections import defaultdict
target = 6
output = []
nums = [3,2,4]
seen = {}

for i, item in enumerate(nums):
    competence = target - item
    if competence in seen:
        output = [seen[competence],i]
        break
    seen[item] = i
print(output)