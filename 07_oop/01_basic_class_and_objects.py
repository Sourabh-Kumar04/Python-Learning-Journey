# Basic Class and Object

# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# class Car:
#     brand = None 
#     model = None

# my_car = Car()
# print(my_car)  # <__main__.Car object at 0x7f1b027fec20>



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyoto", "Corolla")
print(my_car) # <__main__.Car object at 0x7f5ef507bfd0>
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car) # <__main__.Car object at 0x7f5ef507bf10>
print(my_new_car.brand)
print(my_new_car.model)