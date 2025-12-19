n = int(input('enter by user'))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end=' ')
    for k in range(n):
        print('*', end=' ')
    print()
