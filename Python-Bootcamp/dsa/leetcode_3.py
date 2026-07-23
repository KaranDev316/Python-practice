s = "abcabcbb"
set_s = set(s)
result = []
length = 0

for i in range (len(s)):
    left = i + 1
    right = len(s) - 1

    if s[i] == s[left]:
        continue
    while left < right:
        length += 1

print(length)