# n = int(input('enter from user : '))
# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(65-1+i), end="")
#     print()
n = int(input('enter from user : '))
for i in range(1, n+1):
    for j in range(i):
        print(chr(65+j), end="")
    print()
