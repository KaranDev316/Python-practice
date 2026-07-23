s = "abba"
sett = set()
longest = 0
left = 0
for right in range (len(s)):
    while s[right] in sett:
        sett.remove(s[left])
        left += 1
    sett.add(s[right])
    longest = max(longest, right - left + 1)

print(longest)




