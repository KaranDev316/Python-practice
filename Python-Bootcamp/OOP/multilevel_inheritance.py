class GrandParent:
    def work(self):
        print("GrandParent work")

class Parent(GrandParent):
    def work(self):
        print("Parent work")

class Child(Parent):
    def work(self):
        print("Child work")

alfred = Child()

GrandParent.work(alfred)
Parent.work(alfred)
alfred.work()