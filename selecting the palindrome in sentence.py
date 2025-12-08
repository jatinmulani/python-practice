a = input('enter from user :')
for c in a.split():
    if (c[:] == c[::-1]):
        print(c)
