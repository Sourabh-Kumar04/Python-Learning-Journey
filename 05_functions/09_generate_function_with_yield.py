# Generate function with yield

# def even_generator(limit):
#     for i in range(2, limit+2, 2): # last parameter is 2 not 1 beacuse last parameter is not inclusive in python
#         # print(i)
#         return i

# def even_generator(limit):
#     li = []
#     for i in range(2, limit+2, 2): 
#         li.append(i)
#     return li  # but we are getting list not numbers like in range 

limit = int(input("Enter a number: "))

def even_generator(limit):
    for i in range(2, limit+2, 2): # last parameter is 2 not 1 beacuse last parameter is not inclusive in python
        yield i # yield also store the state of the function

for num in even_generator(limit):
    print(num)

