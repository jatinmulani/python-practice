n = int(input('enter from user : '))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + n - i - 1 + j), end=" ")
    print()
