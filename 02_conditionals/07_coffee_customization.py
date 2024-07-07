# Coffee Customization

# order_size = input("Choose the size of coffee: \n 1. Large \n 2. Medium \n 3. Small \n").lower()

# if order_size == "large":
#     order = "Large"
# elif order_size == 'medium':
#     order = "Medium"
# elif order_size == "small":
#     order = "Small"
# else:
#     print("Please enter the right choice")
#     exit()


# extra_shot = input("Do you want extra shot of 'espresso' \n 1. Yes \n 2. No \n").lower()

# if extra_shot == "yes":
#     print("Your order is ", order, "coffee with extra shot of espresso.")
# elif extra_shot == "no":
#     print("Your order is ", order, "coffee with no extra shot of espresso")
# else:
#     print("Please enter the right choice")


order_size = input("Choose the size of coffee: \n 1. Large \n 2. Medium \n 3. Small \n").lower()

if order_size != "large" and order_size != "medium" and order_size != "small":
    print("Please choose the right size.")  
    exit()

extra_shot = input("Do you want extra shot of 'espresso' \n 1. Yes \n 2. No \n").lower()

if extra_shot == "yes":
    coffee = order_size + " coffee with extra shot."
elif extra_shot == "no":
    coffee = order_size + " coffee"
else:
    print("Enter the right choice")

print("Order:", coffee)