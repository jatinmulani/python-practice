# A
# BC
# DEF
# GHIJ
k = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(chr(65-1+k), end="")
        k += 1
    print("")
