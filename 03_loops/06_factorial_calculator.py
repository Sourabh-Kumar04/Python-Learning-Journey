# Factorial Calulator

number = int(input("Enter a number: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1


print("factorial of ", number, "is ", factorial)  # error in print "number" it always print 0
