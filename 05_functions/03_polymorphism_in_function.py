# Polmorphism in Function

# def multiply(parameter1, parameter2):
#   """Multiplies two numbers or concatenates two strings,
#      or repeats a string based on a number if one is a string and the other is a number.

#   Args:
#       parameter1: The first number or string.
#       parameter2: The second number or string.

#   Returns:
#       The product of the two numbers if they are numbers,
#       the concatenation of the two strings otherwise,
#       or the repeated string if one is a string and the other is a number.
#   """

#   try:
#     # Convert inputs to numbers if possible
#     num1 = float(parameter1)
#     num2 = float(parameter2)
#     return num1 * num2
#   except ValueError:  # Catch conversion errors (non-numeric input)
#     if isinstance(parameter1, str) and isinstance(parameter2, (int, float)):
#       # Repeat the string based on the number
#       return parameter1 * parameter2
#     else:
#       # Concatenate other string combinations
#       return str(parameter1) + str(parameter2)

# # Get user input
# parameter1 = input("Enter the first number/string: ")
# parameter2 = input("Enter the second number/string: ")

# print(multiply(parameter1, parameter2))



# def multiply(parameter1, parameter2):
#   """Multiplies two numbers or concatenates two strings,
#      or repeats a string based on a number if one is a string and the other is a number.

#   Args:
#       parameter1: The first number or string.
#       parameter2: The second number or string.

#   Returns:
#       The product of the two numbers if they are numbers,
#       the concatenation of the two strings otherwise,
#       or the repeated string if one is a string and the other is a number.
#   """

#   try:
#     # Convert inputs to numbers if possible (for multiplication)
#     num1 = float(parameter1)
#     num2 = float(parameter2)
#     return num1 * num2
#   except ValueError:  # Catch conversion errors (non-numeric input)
#     if isinstance(parameter1, str) and isinstance(parameter2, (int, float)):
#       # Repeat the string based on the number
#       return parameter1 * parameter2
#     else:
#       # Concatenate other string combinations
#       return str(parameter1) + str(parameter2)

# # Get user input (handle comma-separated input and potential errors)
# while True:
#   try:
#     parameter1 = input("Enter the first number/string (separate with a comma if repeating a string): ").strip()
#     parameter2 = input("Enter the second number/string: ").strip()
#     # Check for comma separation if repeating a string
#     if isinstance(parameter1, str) and isinstance(parameter2, (int, float)):
#       if "," not in parameter1:
#         raise ValueError("Separate the string and number with a comma for repetition.")
#     break  # Exit the loop if valid input is received
#   except ValueError as e:
#     print(f"Error: {e}. Please try again.")

# print(multiply(parameter1, parameter2))


def multiply(p1,  p2):
    return p1 * p2

print(multiply(8,5))
print(multiply('a',5))
print(multiply(8,'a'))
# print(multiply('b','a'))