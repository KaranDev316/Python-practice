
marks = input("Enter marks sperated by comma: ").split(",")
sum = 0
for mark in marks:
    sum += int(mark)

print(sum)