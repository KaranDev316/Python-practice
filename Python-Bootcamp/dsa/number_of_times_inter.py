from collections import Counter
nums1 = [0,0,1,2]
nums2 = [0,0,0,2]

answer = Counter(nums1)
answer2 = Counter(nums2)
result1 = answer & answer2

final = []
print(result1)

for num, count in result1.items():
    final.append([num] * count)

print(final[0] + final[1])