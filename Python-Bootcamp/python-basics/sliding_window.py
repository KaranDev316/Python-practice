s1 = 'ab'

s2 =  "caaabx"

left = 0
right = len(s1)

print(left)
print(right)

window = []

for left in range(len(s2)):
    window.append(s2[left:right])
    print(window)
    print(left)

    right += 1



