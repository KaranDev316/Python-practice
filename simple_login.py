defined_username = "admin"
defined_password = "abc123"

for i in range(1,4):
    print(i, "attempt(s)")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == defined_username and password == defined_password:
        print("Welcome, {}!".format(username))
        break
    else:
        if i == 3:
            print("You have reached the limit of 3 attempts")
        i = i + 1