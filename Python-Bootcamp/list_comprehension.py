# Exercise 2 on list comprehension
doubles = []
for i in range(1, 11):
    doubles.append(i * 2)
print(doubles)

# Using list comprehension


doubles = [i * 3 for i in range(1, 11)]
print(doubles)