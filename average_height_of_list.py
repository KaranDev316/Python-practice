
marks = input("Enter marks sperated by comma: ").split(",")
sum = 0
length = len(marks)

for mark in marks:
    sum += int(mark)

print(sum)
print(length)