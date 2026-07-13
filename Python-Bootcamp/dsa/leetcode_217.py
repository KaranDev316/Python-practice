from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = False
        nums = Counter(nums)

        for num in nums:
            if nums[num] >= 2:
                result = True
        return result

print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))