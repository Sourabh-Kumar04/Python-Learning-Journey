age = int(input("Enter your Age: "))
day = input("Enter the day: ").lower()
discoun_day = "wednesday"

# if age < 18 :
#     price = 8
# else :
#    price  = 12


# if day == discoun_day :
#     price = price - 2

# print("The price of ticket is " + str(price) + ".")


price = 12  if age >= 18 else 8

# if day == discoun_day:
if day == "wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $", price)
