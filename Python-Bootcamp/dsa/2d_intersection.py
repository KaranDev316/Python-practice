from collections import Counter
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

nums_count = Counter(set(nums))

result1 = []


for i in range(len(nums)):
    print(i)
    print(set(nums[i]))
    result1.append(set(nums[i]))


