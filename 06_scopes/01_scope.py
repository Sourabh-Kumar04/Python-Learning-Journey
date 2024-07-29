# Scopes

# username = "rasocode"

# def func():
#     # username = "raso"
#     print(username)

# print(username)
# func()


x = 99

# def func2(y):
#     z = x + y
#     return z

# result =  func2(1)
# print(result)


# def func3():
#     global x
#     x = 12

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    # f2()
    return f2
f1()

myResult1 = f1()
myResult1()


def rasocoder(num):
    def actual(x):
        return x ** num
    return actual
    
f = rasocoder(2)
g = rasocoder(3)

print(f)
print(g)
print(f(3))  # 9
print(g(3))  # 27