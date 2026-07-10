from collections import Counter
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

result_counter = []
nums_extend = []
for i in range(len(nums)):
    nums_extend.extend(set(nums[i]))

print(nums_extend)



