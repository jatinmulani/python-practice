salary = 1000


def func_add(a, b):
    global salary
    c = a+b
    salary = 500
    print("c values", c, "salary", id(salary), salary)


func_add(10, 20)
print(id(salary))
