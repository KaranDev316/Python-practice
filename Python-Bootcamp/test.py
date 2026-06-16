class Car:
    pass

    def name_car(self, name):
        self.name = name
        print(f"This is my {name}")

# Your code here
car1 = Car()
car2 = Car()


print(car1.name_car("mahindra"))
print(car2.name_car("Toyota"))

# Output should show three DIFFERENT memory addresses