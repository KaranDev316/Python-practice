
student_mark = {
    "alfred" : 93,
    "bob": 40,
    "karan": 50
}

for name, value in student_mark.items():
    if value > 90:
        value = "A+"
    elif value > 80:
        value = "A"
    elif value > 70:
        value = "B+"
    elif value > 60:
        value = "B"
    elif value > 50:
        value = "C"
    elif value > 40:
        value = "D"
    elif value > 30:
        value = "F"
    print(f"{name}: {value}")

