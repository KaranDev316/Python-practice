nums = [100, 4, 200, 1, 3, 2]

set_nums = set(nums)
sequence = set()

for num in nums:
    if (num - 1 in nums) or (num + 1 in nums):
        sequence.add(num)

print(sequence)
print(set_nums)