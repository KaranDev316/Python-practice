

start_point = int(input("Enter the starting point: "))
end_point = int(input("Enter the ending point: "))

for i in range(start_point, end_point+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


