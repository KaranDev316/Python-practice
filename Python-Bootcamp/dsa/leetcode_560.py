nums = [1,2,3,1]
k = 3
count  =  0
sum = 0

for right in range(len(nums)):
    sum += nums[right]
    print(sum)
    if sum == k:
        count += 1

print(count)