class Human:
    def work(self):
        print("Human is working")
class Male:
    def work(self):
        print("Male is working")

class Boy(Human,Male):
    pass
boy = Boy()
boy.work() #print Human is working
Male.work(boy) #print Male is working