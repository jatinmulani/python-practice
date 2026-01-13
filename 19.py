num = int(input('enter from user : '))
i = 2
a = 100
while (i < num):
    if (num % i == 0):
        a = 101
        break
    i += 1
if (a == 100):
    print("prime")
else:
    print('not prime')
# prime number by tushar sir method
