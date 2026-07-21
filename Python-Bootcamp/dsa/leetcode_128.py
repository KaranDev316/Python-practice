nums = [0,3,7,2,5,8,4,6,0,1]

set_nums = set(nums)
sequence = set()

for num in nums:
    if (num - 1 in nums) or (num + 1 in nums):
        sequence.add(num)

print(len(sequence))
