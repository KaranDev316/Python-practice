nums1 =[1,2,3,6]
nums2 =[2,3,4,5]

result = 0
set1 = set(nums1)
set2 = set(nums2)

common = set1 & set2

if common:
    result = sorted(common)[0]
else:
    result = -1

print(result)
