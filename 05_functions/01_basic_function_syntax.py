# Basic Function Syntax

number = int(input("Enter a number: "))

def square_of_number(number):
    # print(f"Square of {number} is {number**2}")
    # print(number ** 2)
    return number ** 2   # result will store the value of square_of_number(number)

# square_of_number(number)
result = square_of_number(number)
print(result)  # None in case of print and value in case of return