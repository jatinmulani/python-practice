# A1 B2 C3
# D4 E5
# F6
a = 1
b = 1
for i in range(1, 4):
    for j in range(1, 4-i+1):
        print(chr(65-1+a), str(b), end=" ")
        a += 1
        b += 1
    print(" ")
