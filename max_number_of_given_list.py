list1 = [19,22,93,64,45,62,7,18,9,10]

maximum = list1[0]

for i in range(1,len(list1)):
    if list1[i] > maximum:
        maximum = list1[i]
print(maximum)
