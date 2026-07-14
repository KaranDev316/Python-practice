from collections import Counter
s = "leetcode"
s2 = Counter(s)

for i, item in enumerate(s2):
    if s2[item] == 1:
        print(i)
        break

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        duplicate = set()
        result = -1

        for item in s:
            if item in seen:
                duplicate.add(item)
            seen.add(item)
        unique_items = seen - duplicate

        for i, item in enumerate(s):
            if item in unique_items:
                result = i
                break

        return result

