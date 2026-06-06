
marks = input("Enter marks sperated by comma: ").split(",")
sum = 0
length = len(marks)

for mark in marks:
    sum += int(mark)
average = sum / length

print(f"The average of total marks is {round(average)}")