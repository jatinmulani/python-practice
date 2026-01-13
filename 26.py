# ******
# *   *
# *  *
# * *
# **
# *
# for i in range(6, 0, -1):
#     for j in range(1, i+1):
#         if (i == 6 or j == 1 or j == i):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")
x = 6
for i in range(1, 7):
    for j in range(1, 7-i+1):
        if (i == 1 or j == 1 or x == j):
            print("*", end="")
        else:
            print(" ", end="")
    x -= 1
    print("")
