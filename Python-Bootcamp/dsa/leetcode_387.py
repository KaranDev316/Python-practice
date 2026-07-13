from collections import Counter
s = "leetcode"
s2 = Counter(s)

for i, item in enumerate(s2):
    if s2[item] == 1:
        print(i)
        break




