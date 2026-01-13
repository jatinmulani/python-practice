
a = int(input('enter from user : '))
b = int(input('enter from user : '))
while (b != 0):
    temp = b
    b = a % b
    a = temp
print(a)
