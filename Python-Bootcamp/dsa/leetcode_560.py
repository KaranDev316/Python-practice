nums = [1,2,3,1]
k = 3
count  =  0
sum = 0
left = 0
right = 0

for i in range(len(nums)):
    sum += nums[left]
    if sum == k:
        count += 1
    while right < len(nums):
        sum += nums[right]
        if sum == k:
            count += 1

        right += 1
    if left == right:
        left += 1

    if sum == k:
        count += 1

print(count)