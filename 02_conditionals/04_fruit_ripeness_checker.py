# Fruit Ripeness Checker

fruit = "Banana"
color = input("Enter the color of fruit: ").lower()
# print(color)

if fruit == "Banana":
    if color == "green":
        print("Unripe")
    elif  color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Please check your color.")
else:
    print("Currently I have no information regarding other fruits except Banana")
