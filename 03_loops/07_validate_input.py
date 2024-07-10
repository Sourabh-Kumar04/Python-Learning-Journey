# Validate Input

while True:
    number = int(input("Enter a number: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")