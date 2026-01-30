# 3rd property ==> paas any function as a argument to another function
def add_two_number(a, b):
    print(a+b)


def add_number(x, y):
    print("x::", x, "y::", y)
    print("in next will get ouput of add _two _number function")
    print(y(10, 20))


z = add_number(90, add_two_number)

print(z)
# saare first class function high order hote hai but saare high order function first class nhi hote
