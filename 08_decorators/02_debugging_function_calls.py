# Debugging Function Calls
#   Problem 2:Create a decorator to print the function and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(F"calling: {func.__name__} with args {args_value} and {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")

greet("raso", greeting="hanji")