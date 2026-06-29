""""
Given two lists, list1 and list2, we need to find elements that exist only in list1 and elements that exist only in list2, respectively.
"""

list1 = [1,2,3]
list2 = [2,4,6]

only_in_list1 = set(list1) - set(list2)
only_in_list2 = set(list2) - set(list1)

print(list(only_in_list1))
print(list(only_in_list2))