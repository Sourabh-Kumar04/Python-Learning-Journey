# Class Method and Self

# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Toyoto", "Corolla")
print(my_car)
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name)  # <bound method Car.full_name of <__main__.Car object at 0x7f1b1766ffd0>>
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car)
# print(my_new_car.brand)
# print(my_new_car.model)
print(my_new_car.full_name) # <bound method Car.full_name of <__main__.Car object at 0x7f1b1766fee0>>
print(my_new_car.full_name())
