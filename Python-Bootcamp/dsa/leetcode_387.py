from collections import Counter
s = "leetcode"
s2 = Counter(s)
result = 0

for item in s2:
    if s2[item] == 1:
        result_item = item
        break
for i in range(len(s)):
    if s[i] == result_item:
        result = i
print(result)