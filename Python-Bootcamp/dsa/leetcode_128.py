nums = [1, 2, 5, 8, 9]

set_nums = set(nums)
sequence = set()
if len(set_nums) == 1:
    print(len(set_nums))

for num in nums:
    if (num - 1 in nums) or (num + 1 in nums):
        sequence.add(num)

print(len(sequence))
f"""
  s = set(nums)
  for num in nums:
        if num - 1 not in s:
            next_num = num + 1
            length = 1
            
            while next_num in s:
                length += 1
                next_num += 1
            longest = max(longest, length)
  return longest



"""