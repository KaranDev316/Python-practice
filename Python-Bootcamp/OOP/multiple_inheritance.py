class Animal:
    def eat(self):
        print("Eating from animal")
class Dog(Animal):
    def eat(self):
        print("Eating from dog")
class Cat(Animal):
    def eat(self):
        print("Eating from cat")
class Bird(Animal):
    pass

bird = Bird()
bird.eat()
