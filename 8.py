n = int(input('enter from user'))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(chr(65+k-1), end=' ')
    print()
