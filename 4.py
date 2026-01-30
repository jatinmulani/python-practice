# function  k andar agr koi variable it is called local scope
# function k bhar agr koi variable usko bhi print kar skte haii it is called global/session/program kahin pr bi print kr skte hai
x = 100
y = 20


def add(a, b):
   
    print("memory of a & b", id(a), id(b))
    a = 40
    print("memory of a and b after update", id(a), id(b))
    c = a+b
    print("total is c", c)


add(x, y)
print("memory adress", id(x), id(y))
