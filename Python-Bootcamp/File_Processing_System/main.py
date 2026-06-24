
print("""Welcome to the File Processing System
Files available to process:
1. Good text
Please enter your choice as it is.

""")
list1 = []
flag = True
try:
    file_name = input("Enter file name: ")
    if file_name == "Good text":

        with open("sample_good.txt","r") as file:
                list1 = [int(line) for line in file]
    else:
        print("Please enter exactly as shown above")
        flag = False


except FileNotFoundError:
        print("File not found")
if flag:
    def calculate_statistics(list1):
        try:
            sum_numbers = 0
            max_number = list1[0]
            min_number = list1[0]
        except IndexError:
            sum_numbers = 0
            max_number = 0
            min_number = 0
        for i in list1:
            sum_numbers = sum_numbers + i

        for i in range(0,len(list1)):
            if list1[i] > max_number:
                max_number = list1[i]
            if list1[i] < min_number:
                min_number = list1[i]

        try:
            average = sum_numbers / len(list1)
            return sum_numbers, average, max_number, min_number
        except ZeroDivisionError:
            print("You cannot divide by zero")
        except UnboundLocalError:
            print("Please enter a number")
    try:
        with open("report.txt","w") as file:
            file.write("Report \n")
            file.write("______ \n")
            file.write("Sum: " + str(calculate_statistics(list1)[0]) + "\n")
            file.write("Average: " + str(calculate_statistics(list1)[1]) + "\n")
            file.write("Max: " + str(calculate_statistics(list1)[2]) + "\n")
            file.write("Min: " + str(calculate_statistics(list1)[3]) + "\n")
    except Exception as e:
        print("Something went wrong")
    else:
       print("Program finished please check the report.txt file")





