def sqaure(num):
    return (num*num)


def cube(x, y):
    print("x::", x, "y::", y)
    print("y return:", y(x))  # y==>square, y(8) y ko sqare h manenge bcz niche cube m y k jagh sqare likha haiv  
    print(x*y(x))


cube(8, sqaure)
