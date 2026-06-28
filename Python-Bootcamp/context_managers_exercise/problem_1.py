
# creating a file and writing list of city names
with open("cities.txt","w") as file:
    file.write("Tokyo \n")
    file.write("Paris \n")
    file.write("New York \n")
    file.write("Sydney \n")

# reading the list of countries and counting them
with open("cities.txt", "r") as f:
    file1 = f.read().splitlines()
    count = 0
    for city in file1:
        count += 1

print(count)