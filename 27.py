# * * * * *
#   *     *
#     *   *
#       * *
#         *
x = 5
for i in range(1, 6):
    for j in range(1, i):
        print(" ", end=" ")

    for k in range(1, 6-i+1):
        if (k == 1 or i == 1 or k == x):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    x -= 1
    print(" ")
