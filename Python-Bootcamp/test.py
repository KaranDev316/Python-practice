class Car:
    def car_details(self,color, brand):
        self.brand = brand
        self.color = color
        print(f"The brand of the car is {self.brand} and the color is {self.color}")

car1 = Car()
car2 = Car()

car1.car_details("red","Kia")
car2.car_details("blue","Toyota")

