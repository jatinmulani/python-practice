# 54321
#   4321
#    321
#     21
#      1
x = 5
for i in range(1, 6):
    temp = x
    for j in range(1, i+1):
        print(" ", end="")
    for k in range(1, 6-i+1):
        print(temp, end="")
        temp -= 1
    x -= 1
    print("")
