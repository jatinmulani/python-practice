n = int(input('enter by user'))
for i in range(1, n):
    for j in range(n-i):
        print(" ", end=' ')
    for j in range(2*i-1):
        if i == n-1 or j == 0 or j == 2*i-2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
