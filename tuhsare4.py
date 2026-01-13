n = int(input('enter from user:'))
for i in range(1, n+1):
    if (i % 2 != 0):
        print("1", end="")
    else:
        print("0", end="")
    for j in range(1, i+1):

        print("")
