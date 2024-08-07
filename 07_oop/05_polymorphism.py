# Polymorphism

# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
    # def raso_brand(self):
        return self.__brand 

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla)  # <__main__.ElectricCar object at 0x7f656499bdf0>
# print(my_tesla.__brand)
print(my_tesla.get_brand())
# print(my_tesla.raso_brand())
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)
print(my_tesla.fuel_type())

my_car = Car("Toyoto", "Corolla")
print(my_car)
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())

my_new_car = Car("Tata", "Safari")
print(my_new_car)
print(my_new_car.get_brand())
print(my_new_car.model)
print(my_new_car.full_name)
print(my_new_car.fuel_type())