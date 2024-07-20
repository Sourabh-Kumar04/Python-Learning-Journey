# Function Returning Multiple Values
import math

def circle_stats(radius):
    # print("hi")
    # return math.pi * radius ** 2
    # print("hi")   # after return function executation stop
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference

radius = int(input("Give the radius of the circle: "))

# print(circle_stats(radius))

a, c = circle_stats(radius)
print("Area:", a,"\nCircumference:", c)

