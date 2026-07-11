from collections import Counter
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
result = []
nums_extend = []
for i in range(len(nums)):
    nums_extend.extend(set(nums[i]))


nums_count = Counter(nums_extend)
print(nums_count)

for key,num in nums_count.items():
    if num == len(nums):
        result.append(key)

print(result)
