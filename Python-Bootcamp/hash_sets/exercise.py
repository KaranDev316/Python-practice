
list1 = set([1, 2, 2, 3, 5])
list2 = set([2, 4, 4, 5, 6])

intersection = list1 & list2
unique_to_1 = list1 - list2
unique_to_2 = list2 - list1

print(f"Common: {list(intersection)}")
print(f"Only in list1: {list(unique_to_1)}")
print(f"Only in list2: {list(unique_to_2)}")