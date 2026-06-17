class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Man(Human):
    pass

alfred = Man("Alfred", 20)
print(alfred.name)