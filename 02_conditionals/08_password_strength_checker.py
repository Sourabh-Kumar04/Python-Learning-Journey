# Password Strength Checker

# password = input("Enter the password: ")

# if len(password) < 6:
#     strength = "Weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("Password strength is : ", strength)


password = input("Enter the password: ")
password_length = len(password)

if password_length < 6:
    strength = "Weak"
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is : ", strength)

