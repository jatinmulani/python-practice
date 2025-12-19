n = int(input('enter from user : '))
for i in range(1, n+1):
    for j in range(1, n*2):
        if (i == n or i+j == n+1 or j-i == n-1):
            print('*', end='')
        else:
            print(end=' ')
    print()
