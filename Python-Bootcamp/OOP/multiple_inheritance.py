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
    def eat(self):
        print("Eating from bird")

animal = Animal()
animal.eat()
dog = Dog()
dog.eat()
