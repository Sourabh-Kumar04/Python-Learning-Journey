# Multiple Inheritance

# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

# Class Inheritance and isinstanceof() function

# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # self.total_car += 1
        Car.total_car += 1

    def get_brand(self):
    # def raso_brand(self):
        return self.__brand 

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod  # ERROR 
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")

# print(my_car.model) # with @property
# print(my_car.model()) # without @property

# print(my_safari.general_description()) # ERROR
# print(Car.general_description())  # ERROR


# print(my_tesla.total_car)
# test = Car("Test", "test")
# print(test.total_car)
# print(Car.total_car)

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car)) # True
# print(isinstance(my_tesla, ElectricCar)) # True

# print(my_tesla)  # <__main__.ElectricCar object at 0x7f656499bdf0>
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.raso_brand())
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())

# my_car = Car("Toyoto", "Corolla")
# print(my_car)
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car)
# print(my_new_car.get_brand())
# print(my_new_car.model)
# print(my_new_car.full_name)
# print(my_new_car.fuel_type())


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla)
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
