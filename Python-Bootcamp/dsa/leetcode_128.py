nums = [1, 2, 5, 8, 9]

set_nums = set(nums)
sequence = set()
if len(set_nums) == 1:
    print(len(set_nums))

for num in nums:
    if (num - 1 in nums) or (num + 1 in nums):
        sequence.add(num)

print(len(sequence))
