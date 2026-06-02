

start_point = int(input("Enter the starting point number: "))
end_point = int(input("Enter the ending point number: "))

if start_point <= end_point:
    for i in range(start_point, end_point+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
else:
    print("Starting point number can not be greater than ending point number")


#Can I move the FizzBuzz logic into a function so that I can call it with different ranges without duplicating code?"

