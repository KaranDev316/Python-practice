print("""Welcome to the File Processing System
Files available to process:
1. Good text
2. Bad text
Please enter your choice as it is.

""")
file_name = input("Enter file name: ")

if file_name == "Good text":
        with open("sample_good.txt","r") as f:
            print(f.read())

