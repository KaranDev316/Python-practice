

nums = [3,2,3]
dict_1 = {}

for num in nums:
    dict_1[num] = dict_1.get(num, 0) + 1

print(dict_1)