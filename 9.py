n = 5

for i in range(n):
    # star pattern
    for j in range(n):
        print("*", end=" ")

    print("|", end=" ")

    # number pattern
    for j in range(1, n + 1):
        print(j, end=" ")

    print("|", end=" ")

    # alphabet pattern
    for j in range(n):
        print(chr(65 + j), end=" ")

    print()
