for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(" ", end="")
    for k in range(1, 2*i-1):
        print("*", end="")
for i in range(2, 5):
    for j in range(1, 5):
        print("*", end="")
    for k in range(1, 2*i+1):
        print("*", end="")
    print("")
